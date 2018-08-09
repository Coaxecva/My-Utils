#!/usr/bin/python

import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def sumzip(*items):
    return [sum(values) for values in zip(*items)]

N = 4
input_reads = (33073989, 37029220, 32179464 , 27074220)
ngmlr_primary_alignments = (28421152, 30963342, 27211544, 23801694)
ngmlr_secondary_alignments = (0, 0, 0, 0)
ngmlr_supplementary_alignments = (4180217, 4361527, 3845364, 4553711)
ngmlr_unmapped_alignments = (4648243, 6060566, 4963079, 3269088)

bwamem_primary_alignments = (30468091, 33283398, 29287574, 25433384)
bwamem_secondary_alignments = (0, 0, 0, 0)
bwamem_supplementary_alignments = (7493561, 8427031, 7305036, 7567083)
bwamem_unmapped_alignments = (2605898, 3745822, 2891890, 1640836)

minimap2_primary_alignments = (29753261, 32350372, 28545372, 25022173)
minimap2_secondary_alignments = (7197847, 7180119, 7107478, 6605139)
minimap2_supplementary_alignments = (2143555, 2372140, 2288921, 2125729)
minimap2_unmapped_alignments = (3320728, 4678848, 3634092, 2052047)

ind = np.arange(N) 
width = 0.18       
delta = 0.03

plt.bar(ind, input_reads, width-delta, color='lightcoral', label='input reads')

plt.bar(ind + width, ngmlr_primary_alignments, width-delta, color='dodgerblue', label='primary alignments')
plt.bar(ind + width, ngmlr_unmapped_alignments, width-delta, color='grey', bottom=ngmlr_primary_alignments, label='unmmaped reads')
plt.bar(ind + width, ngmlr_supplementary_alignments, width-delta, color='orange', bottom=sumzip(ngmlr_primary_alignments, ngmlr_unmapped_alignments), label='supplementary alignments')
plt.bar(ind + width, ngmlr_secondary_alignments, width-delta, color='seagreen', bottom=sumzip(ngmlr_primary_alignments, ngmlr_supplementary_alignments, ngmlr_unmapped_alignments), label='secondary alignments')

for i, v in enumerate(ngmlr_primary_alignments):
    plt.text(i+width-delta, v/3.0,  'NGMLR', color='black', fontweight='semibold', rotation=90)

plt.bar(ind + 2*width, bwamem_primary_alignments, width-delta, color='dodgerblue')
plt.bar(ind + 2*width, bwamem_unmapped_alignments, width-delta, color='grey', bottom=bwamem_primary_alignments)
plt.bar(ind + 2*width, bwamem_supplementary_alignments, width-delta, color='orange', bottom=sumzip(bwamem_primary_alignments, bwamem_unmapped_alignments))
plt.bar(ind + 2*width, bwamem_secondary_alignments, width-delta, color='seagreen', bottom=sumzip(bwamem_primary_alignments, bwamem_supplementary_alignments, bwamem_unmapped_alignments))

for i, v in enumerate(bwamem_primary_alignments):
    plt.text(i+2*width-delta, v/3.0,  'BWAMEM', color='black', fontweight='semibold', rotation=90)

plt.bar(ind + 3*width, minimap2_primary_alignments, width-delta, color='dodgerblue')
plt.bar(ind + 3*width, minimap2_unmapped_alignments, width-delta, color='grey', bottom=minimap2_primary_alignments)
plt.bar(ind + 3*width, minimap2_supplementary_alignments, width-delta, color='orange', bottom=sumzip(minimap2_primary_alignments, minimap2_unmapped_alignments))
plt.bar(ind + 3*width, minimap2_secondary_alignments, width-delta, color='seagreen', bottom=sumzip(minimap2_primary_alignments, minimap2_supplementary_alignments, minimap2_unmapped_alignments))

for i, v in enumerate(minimap2_primary_alignments):
    plt.text(i+3*width-delta, v/3.0,  'MINIMAP2', color='black', fontweight='semibold', rotation=90)

plt.ylabel('Number of reads')
plt.title('Read mapping statistics')
plt.xticks(ind + 1.5*width, ('LCL5', 'LCL6', 'LCL7', 'LCL8'))
plt.legend(loc='best')
plt.tight_layout()
plt.show()