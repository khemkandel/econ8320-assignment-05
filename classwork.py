import re


# mystring="1-401-402-4022"
# re.search(r"(1-)?(\b[1-9]\d{2}\b)-(\b\d{3}\b)-(\b\d{4}\b)",mystring)

mystring="6708 Pine Street,Omaha, NE 68182"
re.search(r"([,]\w+[,]\s+\w{2}\s)",mystring)