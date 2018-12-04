
# python-qt-mvc

examples using python-qt's MVC framework for GUI applications

## `example-no-db.py`

This example creates a conversation view from `QAbstractListModel` and a view function from `QListView` to show a toy list of messages / conversation view. By interacting directly with the model object, we can have it "automatically" update just the UI elements that need updating via signals/slots. This is done via the `dataChanged` signal (in `setData`) and using utility methods like [`QAbstractListModel.beginInsertRows`](https://doc.qt.io/qt-5/qabstractitemmodel.html#beginInsertRows) (in `addData`). 

```
$ python example-no-db.py
I am adding the value: msg4 to my data store
I am changing the value of row 2 to be test in my data store
I am changing the value of row 1 to be test in my data store
```

## Useful References

https://doc.qt.io/qt-5/modelview.html

https://doc.qt.io/archives/qt-4.8/model-view-programming.html (note: outdated and for C++ but useful nonetheless)

https://doc.qt.io/qt-5/qabstractitemmodel.html
