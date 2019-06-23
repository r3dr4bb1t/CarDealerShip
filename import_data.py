import pandas

from search.models import Make, Model, SubModel

df = pandas.read_excel('Car_Category_Data.xlsx')
df.columns = ['make', 'model', 'sub_model']


def get_categories(column):
    return df[column].drop_duplicates()


def save_categories():
    Make.objects.all().delete()
    Model.objects.all().delete()
    SubModel.objects.all().delete()

    for row in df['make'].drop_duplicates():
        Make.objects.create(name=row)

    model_df = df.iloc[:, 0:2].drop_duplicates(subset='model', keep='first')

    for make, model in zip(model_df['make'], model_df['model']):
        Model.objects.create(make=Make.objects.get(name=make), name=model)

    sub_model_df = df.iloc[:, 1:3].drop_duplicates(subset='sub_model', keep='first')

    for model, sub_model in zip(sub_model_df['model'], sub_model_df['sub_model']):
        SubModel.objects.create(model=Model.objects.get(name=model), name=sub_model)



