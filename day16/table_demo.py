from prettytable import PrettyTable

table = PrettyTable()
table.add_column('S.No', ["1", "2", "3"])

table.add_column('Framework', ['React Native', 'Flutter', 'Xamarin'])
table.add_column('Company', ['Meta', 'Google', 'Microsoft'])
table.add_column('Language', ['Javascript', 'Dart', 'C#'])

table.align = 'l'
#table.border = False
table.add_column('S.No', ["1", "2", "3"])
print(table)