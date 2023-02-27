import matplotlib.pyplot as plt
import pandas as pd


# Read the CSV file
df = pd.read_csv('ping_final.csv')
print(df)
ax = plt.gca()
# ax = plt.gca()

# all_plot = df['rtt'].plot(y='rtt', use_index=True) # where the 'Date' is the column with date.
# apnic_plot = df.loc[df['region'] == 'apnic']['rtt'].plot(x='rtt')
# ripe_plot = df.loc[df['region'] == 'ripe']['rtt'].plot(x='rtt')
# afrinic_plot= df.loc[df['region'] == 'afrinic']['rtt'].plot(x='rtt')
# afrinic_plot= df.loc[df['region'] == 'lacnic']['rtt'].plot(x='rtt')


ipv4_df = df.loc[df['type_addr'] == 'IPv4']
# ipv4_plot = ipv4_df[['rtt']].plot.kde(title="Density plot for RTTs - Total Ipv4", ax=ax)
apnic_df = df.loc[df['region'] == 'apnic']
# apnic_df_4 = apnic_df.loc[df['type_addr'] == 'IPv4']
ipv4_plot_apnic = ipv4_df[['rtt']].plot.kde(title="Density plot for RTTs - Total Ipv6", ax=ax)
apnic_df_6 = apnic_df.loc[df['type_addr'] == 'Ipv6']
# ipv6_df = df.loc[df['type_addr'] == 'IPv6']
# ipv6_plot = ipv6_df[['rtt']].plot.kde(title="Density plot for RTTs - Total IPv6", ax=ax)


# df[['rtt']].plot.kde(title="Density plot for RTTs", ax=ax)
# apnic_df = df.loc[df['region'] == 'apnic']
# apnic_df[['rtt']].plot.kde(title="Density plot for RTTs - APNIC", ax=ax)
# ripe_df = df.loc[df['region'] == 'ripe']
# ripe_df[['rtt']].plot.kde(title="Density plot for RTTs - RIPE ", ax=ax)
# afrinic_df = df.loc[df['region'] == 'afrinic']
# afrinic_df[['rtt']].plot.kde(title="Density plot for RTTs -AFRINIC", ax=ax)
# lacnic_df = df.loc[df['region'] == 'afrinic']
# lacnic_df[['rtt']].plot.kde(title="Density plot for RTTs - LACNIC", ax=ax)
plt.show()
