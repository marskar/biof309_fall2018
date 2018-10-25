from importlib import import_module


def get_dataset(name: str):
    """load data from sklearn.datasets"""
    datasets = import_module('sklearn.datasets')
    load_dataset = getattr(datasets, 'load_' + name)
    dataset = load_dataset()
    return dataset


class DatasetInventory:
    """A class to encapsulate scikit-learn datasets"""
    names = set()

    def __init__(self, name: str):
        self.name = name
        ds = get_dataset(name)
        self.data, self.targ, self.cols, self.desc = (ds.get(x) for x in (
            'data', 'target', 'feature_names', 'DESCR'))
        if self.name not in DatasetInventory.names:
            DatasetInventory.names.add(self.name)


def make_generator(names, skip):
    return (DatasetInventory(name=x) for x in names if x not in skip)


ds_names = 'boston', 'diabetes', 'digits', 'iris', 'wine'
overused = 'boston', 'iris', 'wine'

ds_generator = make_generator(ds_names, overused)

diabetes = next(ds_generator)

DatasetInventory.names


def residual_plot(fitted, target, mse=None, r2=None):
    sns.residplot(fitted, target, lowess=True, line_kws={'color': 'red'})
    plt.xlabel('Fitted Values')
    plt.ylabel('Residuals')
    if mse is not None and r2 is not None:
        plt.title(f'MSE = {mse:.0f} and $R^2$ = {r2:.0%}')
    # plt.savefig(filename)
    # In addition to saving the plot, you can show it
    plt.show()


def regression(dataset, model_type='linear_model', model_name='LinearRegression'):
    data = skp.get_data(dataset)
    x_train, x_test, y_train, y_test = skp.split_data(data)
    model = skp.get_model(model_type=model_type, model_name=model_name)
    fit = model.fit(x_train, y_train)
    skp.pickle_model(model=fit, filename=f'{dataset}_{model_name}.pickle')
    predictions = fit.predict(x_test)
    mse = mean_squared_error(y_true=y_test, y_pred=predictions)
    r2 = r2_score(y_true=y_test, y_pred=predictions)
    residual_plot(fitted=predictions,
                  target=y_test,
                  mse=mse, r2=r2,
                  filename=f'{dataset}_{model_name}.png')
    return (f'The {model_name} explained'
            f'{r2:.0%} of the variance ($R^2$)'
            f'in the {dataset} dataset.')


regression()
