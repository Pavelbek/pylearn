#Here we open file1, take text from it. Create new file, write there text from file1 and print text from file2 to console 


def main():
	with open('/home/pavel/test.txt', 'r') as file1:
		file1_text = file1.read()
	with open('/home/pavel/test2.txt', 'w+') as file2:
		file2.write(file1_text)
		file2.seek(0)
		text_file2 = file2.read()
	return text_file2




if __name__ == "__main__":
    print main()
