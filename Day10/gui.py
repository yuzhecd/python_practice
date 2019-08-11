#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 19:25:32
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import tkinter
import tkinter.messagebox

def main():
	flag = True

	# modify the word of label
	def change_label_text():
		nonlocal flag
		flag = not flag
		color, msg = ('red', 'Hello, world!') \
			if flag else ('blue', 'Goodbye, world!')
		label.config(text=msg, fg=color)

	# cofirm to quit
	def confirm_to_quit():
		if tkinter.messagebox.askokcancel('Warm prompt', 'Are you confirm to quit?'):
			top.quit()

	# create top window
	top = tkinter.Tk()
	# set the size of window
	top.geometry('240x160')
	# set the headline of window
	top.title('Gaming')
	# create label object and add to top window
	label = tkinter.Label(top, text='Hello, My world', font='Arial -32', fg='red')
	label.pack(expand=1)
	# create a contain to store button
	panel = tkinter.Frame(top)
	# create button and add to contain assigned
	button_1 = tkinter.Button(panel, text='modify', command=change_label_text)
	button_1.pack(side='left')
	button_2 = tkinter.Button(panel, text='quit', command=confirm_to_quit)
	button_2.pack(side='right')
	panel.pack(side='bottom')
	# start the main loop
	tkinter.mainloop()


if __name__ == '__main__':
	main()
