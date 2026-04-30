import win32com.client
word = win32com.client.Dispatch('Word.Application')
word.Visible = False
doc = word.Documents.Open(r'D:\same-fuzz\fuzz4all-main\fuzz4all-main\4.30 1：21目前进展与后续改进方案.doc')
text = doc.Content.Text
doc.Close(False)
word.Quit()
with open('D:/same-fuzz/doc_content.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done')
