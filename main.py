from datetime import datetime
from typing import Dict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates



def readPanda():
    #data = pd.read_csv('reb82.txt')
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}
    plt.rc('font', **font)
    #data = pd.read_csv('reb2.txt')



    #data = pd.read_csv('reb6taken.txt')
    #data = pd.read_csv('reb6.txt')

    #data = pd.read_csv('last/latencyy6.txt')


    #data = pd.read_csv('var/varpmu.txt')

   # data = pd.read_csv('500mslatency2.txt')


    #data = pd.read_csv('mu/352.txt')

   # data = pd.read_csv('mu/365.txt')

   # data = pd.read_csv('mu2/365pp.txt')

    #data = pd.read_csv('mu2/3105.txt')

   # data = pd.read_csv('mu2/3205.txt')

    #data = pd.read_csv('mu2/36200t.txt')
    #data = pd.read_csv('mu2/355200dist7.txt')

    #data = pd.read_csv('muvar/wsla1paretoavg2m.txt')


    #data = pd.read_csv('muvar/wsla1pareto9530.txt')
    #data = pd.read_csv('muvar/wsla1paretoavg30.txt')
    #data = pd.read_csv('muvar/wsla1pareto95p1m2.txt')

    #data = pd.read_csv('muvar/wsla1pareto951mvar101di2.txt')
    #data = pd.read_csv('muvar/wslanew2.txt')
    #data = pd.read_csv('hetero/heterof.txt')



    #data = pd.read_csv('new/mynew.txt')


    data = pd.read_csv('newmodel/newmodel6.txt')



















    data = data.iloc[::-1].reset_index()
    print(data[' text_payload'])
    print(data[' pod_name'])
    data[' text_payload'] = data[' text_payload'].str.extract('latency is (\d+)')
    data[' text_payload'] = data[' text_payload'].astype(float)


    data['timestamp'] =pd.to_datetime( data['timestamp'])
    m = data['timestamp'].first_valid_index()
    datem = data['timestamp'][m]
    data['timestamp'] = (data['timestamp'] - datem)
    data['timestamp'] = data['timestamp'].dt.seconds
    fig, ax = plt.subplots()
    #ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
    plt.xticks(rotation=45, ha='right')
    your_counter = len(data[data[' text_payload'] > 500])
    #your_counter2 = len(data[' text_payload'].where(data[' text_payload'] > 500))
    print(your_counter)
    #print(your_counter2)
    #data[' text_payload'].hist(bins=100)
    #data[' text_payload'].hist(cumulative=True, bins=200, density =1,  alpha=0.8)##hist(bins=100)
    ax.set_xlabel("Time (sec)", **font)
    ax.set_ylabel("latency (ms)", **font)
    ax.plot( data['timestamp'], data[' text_payload'])
    plt.show()






def getReplicasMinutes():
    # data = pd.read_csv('mazparse.txt')
    # data = pd.read_csv('sknoheart/skewedbpheart.txt')
    # data = pd.read_csv('sknoheart/skewedrange.txt')
    # data = pd.read_csv('newreb/reb2sechearttaken.txt')*
    # data = pd.read_csv('taxisk/sktaxibp.txt')
    # data = pd.read_csv('reb/95reb4s.txt')
    # ata = pd.read_csv('newreb/reb2stakennewnoh.txt')
    # data = pd.read_csv('hetero/heterologsnoheart.txt')
    # data = pd.read_csv('hetero/heteroinit.txt')
    # data = pd.read_csv('hetero/initdelayhetero.txt')
    # data = pd.read_csv('200/2002.txt')
    # data = pd.read_csv('newtaxi/bpsktaxiwh.txt')
    # data = pd.read_csv('taxi/taxi94.txt')
    # data = pd.read_csv('taxi/lineartaxi.txt')
    # data = pd.read_csv('taxisk/sktaxibp.txt')
    # data = pd.read_csv('taxisk/sktaxirange.txt')
    # data = pd.read_csv('taxisk/bpsktaxiwhnr.txt')
    # data = pd.read_csv('newtaxi/bpsktaxiwhnr.txt')
    # data = pd.read_csv('20-8/55.txt')
    # data = pd.read_csv('20-8/44.txt')
    # data = pd.read_csv('20-8/84.txt')
    # data = pd.read_csv('heartbeat/17h.txt')
    # data = pd.read_csv('fh/162.txt')
    # data = pd.read_csv('25-8/92.txt')
    # data = pd.read_csv('reb2.txt')

    # data = pd.read_csv('wsla/wsla1reb2taken.txt')
    # data = pd.read_csv('wsla/wsla15reb2taken.txt')
    # data = pd.read_csv('wsla/wsla15reb2omtaken.txt')

    # data = pd.read_csv('taxiwsla15/wsla15reb2taxi.txt')
    # data = pd.read_csv('wsla/wsla15reb2taken.txt')

    # data = pd.read_csv('wsla05/wsla05reb05taken.txt')

    # data = pd.read_csv('wsla05/wsla05reb05f3.txt')

    # data = pd.read_csv('rebtest/reb2.txt')

    # data = pd.read_csv('wsla05/wsla05reb05taxitaken.txt')
    # data = pd.read_csv('wsla05/wsla05reb05taxinottaken.txt')
    # data = pd.read_csv('wsla05/wsla05reb05taxinottakenf3.txt')
    # data = pd.read_csv('wsla05/wsla05reb05taxinottakenf3pa.txt')

    # data = pd.read_csv('newtest/new945.txt')

    #data = pd.read_csv('reb82.txt')

   # data = pd.read_csv('reb6taken.txt')

    #data = pd.read_csv('reb6.txt')


    # data = pd.read_csv('last/latencyy6.txt')

    #data = pd.read_csv('loop2.txt')

    #"data = pd.read_csv('500mslatency.txt')

    #data = pd.read_csv('mu/352.txt')

    #data = pd.read_csv('mu/365.txt')


    #data = pd.read_csv('mu2/365pp.txt')


    #data = pd.read_csv('mu2/3105.txt')
    #data = pd.read_csv('mu2/3205.txt')

    #data = pd.read_csv('mu2/35225.txt')

    #data = pd.read_csv('mu2/36200t.txt')

    #data = pd.read_csv('mu2/355200dist7.txt')

    #data = pd.read_csv('muvar/wsla1normal.txt')

    #data = pd.read_csv('muvar/wsla1normalavg2m.txt')

    #data = pd.read_csv('muvar/wsla1paretoavg2m.txt')
    #data = pd.read_csv('muvar/wsla1pareto9530.txt')


    #data = pd.read_csv('muvar/wsla1paretoavg30.txt')
    #data = pd.read_csv('muvar/wsla1pareto95p1m2.txt')


    #data = pd.read_csv('muvar/wsla1pareto951mvar101di2.txt')

    #data = pd.read_csv('muvar/wslanew2.txt')

    data = pd.read_csv('newmodel/newmodel6.txt')

    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # data = pd.read_csv('taxi/taxireb2s.txt')

    u = data[' pod_name'].unique()
    print(u)
    totalseconds = 0
    for i in range(len(u)):
        print(u[i])
        h = data[' pod_name'][data[' pod_name'] == u[i]].last_valid_index()
        m = data[' pod_name'][data[' pod_name'] == u[i]].first_valid_index()

        # h = data[' pod_name'].where(data[' pod_name'] == u[i]).last_valid_index()
        # m = data[' pod_name'].where(data[' pod_name'] == u[i]).first_valid_index()
        datem = data['timestamp'][m]
        dateh = data['timestamp'][h]
        print(datem)
        print(dateh)


        t= (datem - dateh).seconds

        print()
        # datetime_obj1 = datetime.strptime(
        #     str(datem)[0:-11], '%Y-%m-%dT%H:%M:%S')
        # datetime_obj2 = datetime.strptime(
        #     str(dateh)[0:-11], '%Y-%m-%dT%H:%M:%S')
        # t = (datetime_obj1 - datetime_obj2).seconds
        totalseconds += t
    print(totalseconds / 60)



def plotByPod():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}
    plt.rc('font', **font)
    data = pd.read_csv('newmodel/newmodel6.txt')

    #data = pd.read_csv('testlatnew.txt')


    data = data.iloc[::-1].reset_index()
    print(data[' text_payload'])
    print(data[' pod_name'])
    data[' text_payload'] = data[' text_payload'].str.extract('latency is (\d+)')
    data[' text_payload'] = data[' text_payload'].astype(float)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    groups = data.groupby(' pod_name')

    num_of_groups = len(groups.groups)
    print(num_of_groups)



    dfs= []

    fig, axs = plt.subplots(num_of_groups, 1, figsize=(30, 20), facecolor='w', edgecolor='k', sharex='all')
    fig.subplots_adjust(hspace=.5, wspace=.001)





    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
    plt.xticks(rotation=45, ha='right')

    for name, group in groups:
        dfs.append(group)

    for i in range(0, num_of_groups):
        axs[i].title.set_text("")
        axs[i].plot(dfs[i]['timestamp'], (dfs[i][' text_payload']))
        #axs[i].grid()
        axs[i].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
        #axs[i].xticks(rotation=45, ha='right')
        axs[i].set_ylabel( "Consumer "  + str(i), **font)

    plt.show()

        #
    # for df in dfs:
    #  # print(df)
    #  # print(type(df))
    #  print(df)
    #  ax.plot(df['timestamp'], df[' text_payload'])
    #  plt.show()



    print("------------------------")
    print(dfs[0])

if __name__=='__main__':

    # readPanda()
    # getReplicasMinutes()
    plotByPod()



