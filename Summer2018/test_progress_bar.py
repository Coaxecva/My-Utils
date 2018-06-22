#pip3 install progressbar33
from time import sleep
import progressbar

bar = progressbar.ProgressBar(maxval=20, \
	widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

bar.start()

for i in range(20):
	bar.update(i+1)
	sleep(0.5)

bar.finish()