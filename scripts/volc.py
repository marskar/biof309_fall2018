class Volcano(object):
    """
    create a Volcano plot from log2(ratios) and corresponding -log10(p_values)
    ToDo: take care of infinite ratios

    e.g. usage
    dict_ = {'p_val': {1: 0.208057931774703, 2: 0.063320586966883294, 3: 0.11424685505629198, 4: 0.46130291511303301, 5: 0.31662387800522196, 6: 0.35821379490648098, 7: 0.0559720700871537, 8: 0.048805611096553, 9: 0.27635717881946303, 336: 7.1364464137191392, 264: 0.50054528789819708, 530: 4.9027283450578603, 83: 4.4128053670050704, 565: 5.7615691096534203}, 'ratio': {1: -0.22443504333496, 2: 0.074678929646808001, 3: 0.27419026692708204, 4: 0.48245075770786605, 5: 0.274400329589845, 6: -0.53869597117106194, 7: 0.13976793819003699, 8: 0.20341746012369896, 9: 0.54393492804633292, 336: 4.2886840820312502, 264: -3.9391211668650299, 530: 4.5683480792575404, 83: 2.5429632663726802, 565: 4.04515149858263}, 's_val': {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 336: 11.159643571086351, 264: 0.0, 530: 6.9983089690857891, 83: 1.0852958656755318, 565: 7.2227303405181722}, 'label': {1: 'CRYAB', 2: 'HDLBP', 3: 'TAF15', 4: 'GNAO1', 5: 'KHSRP', 6: 'HSPA4', 7: 'PABPC1;PABPC4', 8: 'MINOS1', 9: 'SPCS2', 336: 'APOL2', 264: 'WISP3', 530: 'WARS', 83: 'HLA-C', 565: 'GBP1'}}
    df = pd.DataFrame(dict_)
    volc = Volcano(df["ratio"], df["p_val"], df["label"], s_curve_x_axis_overplot=0.5, s_curve_y_axis_overplot=0.5)
    fig = volc.get_fig()

    from Perseus documentation:
    S0: Artificial within groups variance (default: 0).
    It controls the relative importance of t-test p-value and difference between means.
    At s0=0 only the p-value matters, while at nonzero s0 also the difference of means
    plays a role. See Tusher, Tibshirani and Chu (2001) PNAS 98, pp5116-21 for details.
    """

    def __init__(self, ratio, p_val, label=None, s_curve_x_axis_overplot=0.5, s_curve_y_axis_overplot=0.5):
        """
        careful use ratio not difference as in Perseus
        ratio of 0.5 instead of difference -2
        :param ratio: Pandas.Series or Numpy.Array or List of log2(ratios)
        :param p_val: Pandas.Series or Numpy.Array or List of -log10(p-values)
        :param label: Pandas.Series or Numpy.Array or ListOfString
        """
        assert len(ratio) == len(p_val)
        self.df = pd.DataFrame({"ratio": ratio, "p_val": p_val})
        if label is not None:
            self.df["label"] = label
        self.s_curve_y_axis_overplot = s_curve_y_axis_overplot
        self.p_val_cutoff = self.get_p_val_cutoff()
        self.ratio_cutoff = self.get_ratio_cutoff()
        self.df["s_val"] = self.df.apply(self.calc_s_from_row, axis=1)
        self.ratio_for_s = pd.Series(np.linspace(self.df["ratio"].min() - s_curve_x_axis_overplot,
                                                 self.df["ratio"].max() + s_curve_x_axis_overplot, num=1000))
        self.p_for_s_larger_1 = self.ratio_for_s.apply(self.calc_p_for_s_equals_1)

    def get_p_val_cutoff(self):
        """
        p_val_cutoff = 0.05
        pc = 3.5 + median(p_val(50% lowest log2_ratios)) --> is what Jan uses for whatever reason ???
        -log10_pval of 2.0 --> pval of 0.01
        """
        ### hard coded cutoff of 1%
        # return math.log(0.01, 10) * -1
        ### Jan's cutoff, but how to justify???
        quant = self.df["ratio"].quantile(0.5)
        return 2.0 + self.df.loc[self.df["ratio"] < quant, "p_val"].median()

    def get_ratio_cutoff(self):
        """
        log2_ratio_cutoff = 2.0
        ratio_cutoff_high = 2 + median(ratio(50% lowest log10_p_values))
        ratio_cutoff_low = 0.5 - median(ratio(50% lowest log10_p_values))
        """
        ### hard coded cutoff of 2 fold enrichment or depletion
        # return math.log(0.5, 2), math.log(2, 2)
        ### Jan's cutoff, how to justify???
        quant = self.df["p_val"].quantile(0.5)
        median_ = self.df.loc[self.df["p_val"] < quant, "ratio"].median()
        ratio_cutoff_high = 2.0 + median_
        ratio_cutoff_low = -2.0 - median_
        return ratio_cutoff_low, ratio_cutoff_high

    def calc_s_from_row(self, row):
        p_val = row["p_val"]
        ratio = row["ratio"]
        return self.calc_s(p_val, ratio)

    def calc_s(self, p_val, ratio):
        """
        so the algorithmn for finding stuff with s > 1 is:
        discard stuff below the r_cutoff
        discard stuff below the p-val cutoff
        do the calcuation for the stuff above BOTH cutoffs and accept all with s > 1
        s = (p_val - p_val_cutoff) * (ratio - ratio_cutoff)
        :param p_val: Float(-log10 p-value)
        :param ratio: Float(log2 ratio)
        :return: Float
        """
        ratio_cutoff_low, ratio_cutoff_high = self.ratio_cutoff
        ratio_delta = ratio - ratio_cutoff_high
        if ratio_delta < 0:
            return 0
        p_val_delta = p_val - self.p_val_cutoff
        if p_val_delta < 0:
            return 0
        return p_val_delta * ratio_delta

    def calc_p_for_s_equals_1(self, ratio):
        """
        :param ratio: Float(log2 ratio)
        :return: Float
        """
        ratio_cutoff_low, ratio_cutoff_high = self.ratio_cutoff
        ratio_delta_high = ratio - ratio_cutoff_high
        ratio_delta_low = ratio - ratio_cutoff_low

        if ratio > ratio_cutoff_high:
            return (1.0 / ratio_delta_high) + self.p_val_cutoff
        elif ratio < ratio_cutoff_low:
            return (1.0 / (ratio_delta_low * -1)) + self.p_val_cutoff
        else:
            return np.nan

    def get_fig(self, title="Volcano plot", s_value_cutoff=1.0):
        fig, ax1 = plt.subplots(figsize=(12, 12))
        ax1.set_title(title, fontsize=22, fontweight="bold")

        cond_p_val = self.p_for_s_larger_1 <= (self.df["p_val"].max() + self.s_curve_y_axis_overplot)
        cond_pos = self.ratio_for_s > 0
        x1 = self.ratio_for_s[cond_pos & cond_p_val]
        y1 = self.p_for_s_larger_1[cond_pos & cond_p_val]

        cond_neg = self.ratio_for_s < 0
        x2 = self.ratio_for_s[cond_neg & cond_p_val]
        y2 = self.p_for_s_larger_1[cond_neg & cond_p_val]

        x3 = self.df["ratio"]
        y3 = self.df["p_val"]

        ax1.plot(x1, y1, 'r-', x2, y2, 'r-', x3, y3, 'b.', markersize=10)  # , alpha=0.7)
        ax1.set_xlabel('log2(ratio)', fontsize=20)
        ax1.set_ylabel('-log10(p-value)', fontsize=20)

        if "label" in self.df.columns:
            cond = self.df["s_val"] >= s_value_cutoff
            for index_, row in self.df[cond].iterrows():
                label = row["label"]
                x_coord = row["ratio"]
                y_coord = row["p_val"]
                ax1.annotate(label, xy=(x_coord, y_coord), xycoords='data', xytext=(5, 5),
                             textcoords='offset points', arrowprops=dict(arrowstyle="-"), fontsize=12)

        return fig