import json
import pandas as pd

jsontxt = '{                                                                                                                        \
           "foo":                                                                                                                   \
               {                                                                                                                    \
               "col1" : {"row1": 1, "row2": 2, "row3": 3, "row4": 4, "row5": 5, "row6": 6},                                         \
               "col2" : {"row6": 6, "row5": 5, "row4": 4, "row3": 3, "row2": 2, "row1": 1}                                          \
                }                                                                                                                   \
           }'              

jsondict = json.loads(jsontxt)
table = pd.DataFrame(jsondict['foo'])
print(table)

# Define a function to convert the time slots to the categories
def category(element):
    if element < '4':
        return 'a'
    return 'b'


table['new1'] = table.index.str[-1]
print("\n", table)

table['new2'] = table['new1'].apply(category)
print("\n", table)


pt = table.pivot_table(index='new2', aggfunc=sum, fill_value=0)
print("\n", pt)

jsonOutput = pt.to_dict()
print("\n", jsonOutput)
