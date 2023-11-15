# Практическое задание 1, Чераева, РИМ-220907

В данной работе в качестве датасета был выбран набор данных Rotten tomatoes.

В папке scripts/data_scripts представлены файлы, необходимые для того, чтобы загрузить набор данных - get_data.py, а также data_preprocessing.ipynb, где была рассмотрена обработка информации и выбор признаков. Все полученные данные располагались в папку data.

Файлы, представленные в папке scripts/data_processing использовались в процессе создания пайплайна обработки данных. С их помощью из сырых данных выделялись необходимые признаки, заполнялись пропущенные значения, категориальные данные преобразовывались в числовые, далее все делилось на тренировочную и тестовую части.

В папке scripts/model_scripts представлены файлы, используемые для обучения модели и ее оценки. В качестве классификатора была выбрана модель DecisionTreeClassifier, так как она показывала наибольший результат при предварительной оценке моделей.

Результат оценки работы модели представлен в файле metrics.json, расположенном в папке evaluate.
