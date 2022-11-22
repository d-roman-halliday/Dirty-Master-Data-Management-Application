'''
@author: davidroman-halliday
'''
import uuid

from . import beautify_html_table

class item:
    """A common reporting set of attributes to iterate over for multiple data sets to be returned in a page"""
    def __init__(self,
                title,
                dataFrame = None,
                introText : str = None,
                introTextIsHTML : bool = False,
                outroText : str = None,
                outroTextIsHTML : bool = False,
                htmlTable : str = None,
                htmlTableID : str = None,
                htmlTableTitlesCentered : bool = True,
                htmlTableCsvDownload : bool = True
                ):

        if htmlTableID is None:
            htmlTableID = uuid.uuid4()

        self.title = title
        self.dataFrame = dataFrame

        self.introText = introText
        self.introTextIsHTML = introTextIsHTML
        self.outroText = outroText
        self.outroTextIsHTML = outroTextIsHTML

        self.htmlTable = htmlTable
        self.htmlTableID = htmlTableID
        self.htmlTableTitlesCentered = htmlTableTitlesCentered
        self.htmlTableCsvDownload = htmlTableCsvDownload

    def convertToBeautifulHTML(self):
        self.htmlTable = beautify_html_table(
            html_table = self.dataFrame.to_html(index = False),
            table_id = self.htmlTableID,
            center_headings = self.htmlTableTitlesCentered
            )

if __name__ == '__main__':
    pass