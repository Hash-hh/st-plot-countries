import streamlit as st
import plotly.graph_objects as go
import os
import pandas as pd
from stream_funcs import countries_from_multiselect
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

print(os.environ.get('PYTHONPATH'))

# Initialize session state if it hasn't been initialized
if 'chem_unit_price' not in st.session_state:
    st.session_state.chem_unit_price = None

if 'synth_chem_df_list' not in st.session_state:
    st.session_state.synth_chem_df_list = []

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False


def run_app():


    st.title("Chemical Query")

    # Text Input
    chem = st.text_input("Enter the Chemical Name:")

    # Radio button
    options = ["Original Data", "GPT Enriched"]
    radio_button = st.radio("Pick a Database:", options)

    pubchem = False
    partial = False

    if radio_button == "GPT Enriched":
        # Checkbox
        pubchem = st.checkbox("PubChem Synonyms")
        partial = st.checkbox("Allow Partial Match")

    if st.button('Submit'):
        st.session_state.button_clicked = True


    # Submit Button
    if st.session_state.button_clicked:

        # Multi-select for countries
        countries = st.multiselect('Select Countries',
                                   [
                                       "🇦🇫 - Afghanistan", "🇦🇱 - Albania", "🇩🇿 - Algeria", "🇦🇩 - Andorra",
                                       "🇦🇴 - Angola", "🇦🇬 - Antigua and Barbuda", "🇦🇷 - Argentina",
                                       "🇦🇲 - Armenia", "🇦🇺 - Australia", "🇦🇹 - Austria", "🇦🇿 - Azerbaijan",
                                       "🇧🇸 - Bahamas", "🇧🇭 - Bahrain", "🇧🇩 - Bangladesh", "🇧🇧 - Barbados",
                                       "🇧🇾 - Belarus", "🇧🇪 - Belgium", "🇧🇿 - Belize", "🇧🇯 - Benin", "🇧🇹 - Bhutan",
                                       "🇧🇴 - Bolivia", "🇧🇦 - Bosnia and Herzegovina", "🇧🇼 - Botswana",
                                       "🇧🇷 - Brazil", "🇧🇳 - Brunei", "🇧🇬 - Bulgaria", "🇧🇫 - Burkina Faso",
                                       "🇧🇮 - Burundi", "🇨🇻 - Cape Verde", "🇰🇭 - Cambodia", "🇨🇲 - Cameroon",
                                       "🇨🇦 - Canada", "🇨🇫 - Central African Republic", "🇹🇩 - Chad", "🇨🇱 - Chile",
                                       "🇨🇳 - China", "🇨🇴 - Colombia", "🇰🇲 - Comoros", "🇨🇬 - Congo (Republic)",
                                       "🇨🇩 - Congo (DRC)", "🇨🇷 - Costa Rica", "🇭🇷 - Croatia", "🇨🇺 - Cuba",
                                       "🇨🇾 - Cyprus", "🇨🇿 - Czech Republic", "🇩🇰 - Denmark", "🇩🇯 - Djibouti",
                                       "🇩🇲 - Dominica", "🇩🇴 - Dominican Republic", "🇪🇨 - Ecuador", "🇪🇬 - Egypt",
                                       "🇸🇻 - El Salvador", "🇬🇶 - Equatorial Guinea", "🇪🇷 - Eritrea",
                                       "🇪🇪 - Estonia", "🇸🇿 - Eswatini", "🇪🇹 - Ethiopia", "🇫🇯 - Fiji", "🇫🇮 - Finland",
                                       "🇫🇷 - France", "🇬🇦 - Gabon", "🇬🇲 - Gambia",
                                       "🇬🇪 - Georgia", "🇩🇪 - Germany", "🇬🇭 - Ghana", "🇬🇷 - Greece", "🇬🇩 - Grenada",
                                       "🇬🇹 - Guatemala", "🇬🇳 - Guinea", "🇬🇼 - Guinea-Bissau",
                                       "🇬🇾 - Guyana", "🇭🇹 - Haiti", "🇭🇳 - Honduras", "🇭🇺 - Hungary", "🇮🇸 - Iceland",
                                       "🇮🇳 - India", "🇮🇩 - Indonesia", "🇮🇷 - Iran",
                                       "🇮🇶 - Iraq", "🇮🇪 - Ireland", "🇮🇱 - Israel", "🇮🇹 - Italy", "🇨🇮 - Ivory Coast",
                                       "🇯🇲 - Jamaica", "🇯🇵 - Japan", "🇯🇴 - Jordan",
                                       "🇰🇿 - Kazakhstan", "🇰🇪 - Kenya", "🇰🇮 - Kiribati", "🇽🇰 - Kosovo", "🇰🇼 - Kuwait",
                                       "🇰🇬 - Kyrgyzstan", "🇱🇦 - Laos", "🇱🇻 - Latvia",
                                       "🇱🇧 - Lebanon", "🇱🇸 - Lesotho", "🇱🇷 - Liberia", "🇱🇾 - Libya",
                                       "🇱🇮 - Liechtenstein", "🇱🇹 - Lithuania", "🇱🇺 - Luxembourg", "🇲🇬 - Madagascar",
                                       "🇲🇼 - Malawi", "🇲🇾 - Malaysia", "🇲🇻 - Maldives", "🇲🇱 - Mali", "🇲🇹 - Malta",
                                       "🇲🇭 - Marshall Islands", "🇲🇷 - Mauritania", "🇲🇺 - Mauritius",
                                       "🇲🇽 - Mexico", "🇫🇲 - Micronesia", "🇲🇩 - Moldova", "🇲🇨 - Monaco",
                                       "🇲🇳 - Mongolia", "🇲🇪 - Montenegro", "🇲🇦 - Morocco", "🇲🇿 - Mozambique",
                                       "🇲🇲 - Myanmar", "🇳🇦 - Namibia", "🇳🇷 - Nauru", "🇳🇵 - Nepal", "🇳🇱 - Netherlands",
                                       "🇳🇿 - New Zealand", "🇳🇮 - Nicaragua", "🇳🇪 - Niger",
                                       "🇳🇬 - Nigeria", "🇰🇵 - North Korea", "🇳🇴 - Norway", "🇴🇲 - Oman", "🇵🇰 - Pakistan",
                                       "🇵🇼 - Palau", "🇵🇸 - Palestine", "🇵🇦 - Panama",
                                       "🇵🇬 - Papua New Guinea", "🇵🇾 - Paraguay", "🇵🇪 - Peru", "🇵🇭 - Philippines",
                                       "🇵🇱 - Poland", "🇵🇹 - Portugal", "🇶🇦 - Qatar", "🇷🇴 - Romania",
                                       "🇷🇺 - Russia", "🇷🇼 - Rwanda", "🇰🇳 - Saint Kitts and Nevis", "🇱🇨 - Saint Lucia",
                                       "🇻🇨 - Saint Vincent and the Grenadines", "🇼🇸 - Samoa",
                                       "🇸🇲 - San Marino", "🇸🇹 - São Tomé and Príncipe", "🇸🇦 - Saudi Arabia",
                                       "🇸🇳 - Senegal", "🇷🇸 - Serbia", "🇸🇨 - Seychelles", "🇸🇱 - Sierra Leone",
                                       "🇸🇬 - Singapore", "🇸🇰 - Slovakia", "🇸🇮 - Slovenia", "🇸🇧 - Solomon Islands",
                                       "🇸🇴 - Somalia", "🇿🇦 - South Africa", "🇰🇷 - South Korea",
                                       "🇸🇸 - South Sudan", "🇪🇸 - Spain", "🇱🇰 - Sri Lanka", "🇸🇩 - Sudan",
                                       "🇸🇷 - Suriname", "🇸🇪 - Sweden", "🇨🇭 - Switzerland", "🇸🇾 - Syria",
                                       "🇹🇯 - Tajikistan", "🇹🇿 - Tanzania", "🇹🇭 - Thailand", "🇹🇱 - Timor-Leste",
                                       "🇹🇬 - Togo", "🇹🇴 - Tonga", "🇹🇹 - Trinidad and Tobago",
                                       "🇹🇳 - Tunisia", "🇹🇷 - Turkey", "🇹🇲 - Turkmenistan", "🇹🇻 - Tuvalu",
                                       "🇺🇬 - Uganda", "🇺🇦 - Ukraine", "🇦🇪 - United Arab Emirates",
                                       "🇬🇧 - United Kingdom", "🇺🇸 - United States", "🇺🇾 - Uruguay", "🇺🇿 - Uzbekistan",
                                       "🇻🇺 - Vanuatu", "🇻🇦 - Vatican City", "🇻🇪 - Venezuela",
                                       "🇻🇳 - Vietnam", "🇾🇪 - Yemen", "🇿🇲 - Zambia", "🇿🇼 - Zimbabwe",

                                       "EU", "Europe", "America", "Asia", "Africa", "Oceania", "World",
                                       "Middle East"
                                   ],
                                   [
                                       "🇦🇹 - Austria", "🇧🇪 - Belgium", "🇧🇬 - Bulgaria", "🇭🇷 - Croatia", "🇨🇾 - Cyprus",
                                       "🇨🇿 - Czech Republic", "🇩🇰 - Denmark",
                                       "🇪🇪 - Estonia", "🇫🇮 - Finland", "🇫🇷 - France", "🇩🇪 - Germany", "🇬🇷 - Greece",
                                       "🇭🇺 - Hungary", "🇮🇪 - Ireland", "🇮🇹 - Italy",
                                       "🇱🇻 - Latvia", "🇱🇹 - Lithuania", "🇱🇺 - Luxembourg", "🇲🇹 - Malta",
                                       "🇳🇱 - Netherlands", "🇵🇱 - Poland", "🇵🇹 - Portugal",
                                       "🇷🇴 - Romania", "🇸🇰 - Slovakia", "🇸🇮 - Slovenia", "🇪🇸 - Spain", "🇸🇪 - Sweden"
                                   ]
                                   )

        countries = countries_from_multiselect(countries)
        print("countries: ", countries)


        # initialize the download dataframe
        df_download = pd.DataFrame()
        df_download.drop(df_download.index, inplace=True)

        # List all files that match the pattern
        matching_files = [f for f in os.listdir('synthesis data') if f.startswith(f"{chem}_st")]
        # matching_files = ['posaconazole_st1.csv']
        print("matching files: ", matching_files)

        for synthesis_file in matching_files:

            # look for the synthesis csv file for chem to find the ingredients
            # synthesis_file = f'synthesis data/{chem}_st1.csv'
            synth_df = pd.read_csv(f'synthesis data/{synthesis_file}', encoding='latin1')

            # st.write(f"{synthesis_file.replace('.csv', '')} Data", synth_df)

            gd = GridOptionsBuilder.from_dataframe(synth_df)
            gd.configure_selection(selection_mode='multiple', use_checkbox=True
                                   , pre_select_all_rows=True
                                   )
            gridoptions = gd.build()

            grid_table = AgGrid(synth_df, height=250, gridOptions=gridoptions,
                                update_mode=GridUpdateMode.SELECTION_CHANGED)

            # st.write('## Selected')
            selected_row = grid_table["selected_rows"]

            synth_dict = synth_df.set_index('raw_material')['cid'].to_dict()

            if selected_row != []:

                print("selected_row: ", selected_row)
                df_selected_row = pd.DataFrame(selected_row)
                # st.write("df_selected_row", df_selected_row)
                print("df_selected_row: ", df_selected_row.columns)
                df_selected_row = df_selected_row[['raw_material', 'cid']]

                # st.write(df_selected_row)


                synth_dict = df_selected_row.set_index('raw_material')['cid'].to_dict()

            for synth_chem in synth_dict.keys():
                # synth_chem_df = find_matching_chemicals_from_cid(synth_dict[synth_chem])
                # synth_chem_df = synth_chem_df[['date', 'unit_value_usd', 'country']]
                #
                # # export to csv
                # synth_chem_df.to_csv(f'github upload data/{synth_chem}_synthesis.csv', index=False)

                # load the data
                synth_chem_df = pd.read_csv(f'github upload data/{synth_chem}_synthesis.csv')

                synth_chem_df = synth_chem_df[synth_chem_df['country'].isin(countries)]
                synth_chem_df = synth_chem_df[['date', 'unit_value_usd']]

                print(f"synth_chem_df of {synth_chem} \n", synth_chem_df.head())

                # converting 'Date' to datetime and setting as index
                synth_chem_df['date'] = pd.to_datetime(synth_chem_df['date'])
                synth_chem_df.set_index('date', inplace=True)

                # cleaning the data
                # # Converting everything to Kgs
                # synth_chem_df.loc[synth_chem_df['Unit'] == 'GMS', 'Unit_FOB_Rate'] /= 1000
                # synth_chem_df.loc[synth_chem_df['Unit'] == 'GMS', 'Unit'] = 'KGS'

                # remove outliers
                synth_chem_df['unit_value_usd'] = synth_chem_df['unit_value_usd'].astype(float)
                lower_percentile = 25
                upper_percentile = 75
                lower_threshold = synth_chem_df['unit_value_usd'].quantile(lower_percentile / 100)
                upper_threshold = synth_chem_df['unit_value_usd'].quantile(upper_percentile / 100)

                data_cleaned = synth_chem_df[(synth_chem_df['unit_value_usd'] >= lower_threshold) & (synth_chem_df['unit_value_usd'] <= upper_threshold)]

                # resampling and forward filling
                data_resampled = data_cleaned.resample('D').last()
                data_resampled = data_resampled.interpolate(method='linear')

                st.session_state.synth_chem_df_list.append(data_resampled)

                temp_df = data_resampled.copy()
                temp_df.columns = [synth_chem]
                df_download = pd.concat([df_download, temp_df], axis=1)

            # st.write(st.session_state.synth_chem_df_list)

            # plotting
            fig_prec = go.Figure()

            for synth_chem, data in zip(synth_dict.keys(), st.session_state.synth_chem_df_list):
                smooth_rate = data[['unit_value_usd']].rolling(10).mean().dropna()

                # Add line plot for connecting the data points
                fig_prec.add_trace(go.Scatter(x=data.index, y=smooth_rate['unit_value_usd'], mode='lines',
                                         name=f"{synth_chem}"))

            # Set layout
            fig_prec.update_layout(title=f"{synthesis_file.replace('.csv', '')}", xaxis_title='Date', yaxis_title='FOB Price',
                              plot_bgcolor='rgba(0, 0, 0, 0)')

            # Display the plot
            st.plotly_chart(fig_prec, use_container_width=True)

            st.session_state.synth_chem_df_list = []

        if st.button('Download'):

            # get data from the download_dict
            st.write("### Downloading the chemical dataframe")
            st.write("file name: ", f'{chem}_synthesis_data.csv')
            st.write("file type: ", 'text/csv')
            st.write("file size: ",
                     round(df_download.to_csv().encode('utf-8').__sizeof__() / (1024 * 1024), 2),
                     "Megabytes")
            st.download_button(
                label="Download data as CSV",
                data=df_download.to_csv(),
                file_name=f'{chem}_synth_api.csv',
                mime='text/csv',
            )

run_app()