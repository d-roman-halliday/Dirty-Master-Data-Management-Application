'''
Created on 16 Jul 2022

@author: davidroman-halliday
'''
class item:
    """A common reporting set of attributes to iterate over for multiple data sets to be returned in a page"""
    def __init__(self,
                title : str = None,
                DataFrame = None,
                DataFrameID : str = None,
                DataFrameTitlesCentered : bool = True,
                text : str = None,
                html : str = None
                ):
        self.title = title
        self.DataFrame = DataFrame
        self.DataFrameID = DataFrameID
        self.DataFrameTitlesCentered = DataFrameTitlesCentered
        self.text = text
        self.html = html

if __name__ == '__main__':
    pass