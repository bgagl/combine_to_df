import pandas as pd
import os


def make_df_from_files(folder_path='/Users/bg/PycharmProjects/Py_SLR_v0.01/simulation_output_files/Freq_lex_datasets/'):
    files = [f for f in os.listdir(folder_path) if f.startswith('Most_frequent_N_')]
    c = 0
    for file in files:
        print(file)
        file_list = file.split("_")
        tmp = pd.read_csv(folder_path + file)

        if c == 0:
            data_all = pd.concat([tmp['string'], tmp['in_lexicon'], tmp['ope_norm'], tmp['ape_norm'],
                                  tmp['spe_norm']], axis=1)  # tmp['lexicality'],
            print(data_all['in_lexicon'].value_counts())
            data_all.columns.values[3] += ("_" + file_list[3])
            data_all.columns.values[4] += ("_" + file_list[3])
            data_all.columns.values[1] += ("_" + file_list[3])
            data_all.columns.values[2] += ("_" + file_list[3])

            c = 1
            data_all.to_csv("/Users/bg/PycharmProjects/combine_to_df/output/most_freq_all_pe.csv")
        else:
            data_all = pd.read_csv("/Users/bg/PycharmProjects/combine_to_df/output/most_freq_all_pe.csv")
            data_all = data_all.iloc[:, 1:]
            tmp1 = pd.concat([tmp['in_lexicon'], tmp['ope_norm'], tmp['ape_norm'], tmp['spe_norm']],
                             axis=1)
            print(tmp1['in_lexicon'].value_counts())
            tmp1.columns.values[3] += ("_" + file_list[3])
            tmp1.columns.values[0] += ("_" + file_list[3])
            tmp1.columns.values[1] += ("_" + file_list[3])
            tmp1.columns.values[2] += ("_" + file_list[3])

            # data_all.join(tmp1.set_index("string"), on="string")

            data_new = pd.concat([data_all, tmp1], axis=1)
            # print(data_new['lexicality'].value_counts())

            data_new.to_csv("/Users/bg/PycharmProjects/combine_to_df/output/most_freq_all_pe.csv")


def make_df_from_files_rnd(
        folder_path='/Users/bg/PycharmProjects/Py_SLR_v0.01/simulation_output_files/Freq_lex_datasets/'):
    files = [f for f in os.listdir(folder_path) if f.startswith('Random_N_')]
    c = 0
    for file in files:
        print(file)
        file_list = file.split("_")
        tmp = pd.read_csv(folder_path + file)

        if c == 0:
            data_all = pd.concat([tmp['string'], tmp['in_lexicon'], tmp['ope_norm'], tmp['ape_norm'],
                                  tmp['spe_norm']], axis=1)
            print(data_all['in_lexicon'].value_counts())
            data_all.columns.values[3] += ("_" + file_list[2] + "_" + file_list[3])
            data_all.columns.values[4] += ("_" + file_list[2] + "_" + file_list[3])
            data_all.columns.values[1] += ("_" + file_list[2] + "_" + file_list[3])
            data_all.columns.values[2] += ("_" + file_list[2] + "_" + file_list[3])

            c = 1
            data_all.to_csv("/Users/bg/PycharmProjects/combine_to_df/output/rnd_all_pe.csv")
        else:
            data_all = pd.read_csv("/Users/bg/PycharmProjects/combine_to_df/output/rnd_all_pe.csv")
            data_all = data_all.iloc[:, 1:]
            tmp1 = pd.concat([tmp['in_lexicon'], tmp['ope_norm'], tmp['ape_norm'], tmp['spe_norm']],
                             axis=1)
            print(tmp1['in_lexicon'].value_counts())
            tmp1.columns.values[3] += ("_" + file_list[2] + "_" + file_list[3])
            tmp1.columns.values[0] += ("_" + file_list[2] + "_" + file_list[3])
            tmp1.columns.values[1] += ("_" + file_list[2] + "_" + file_list[3])
            tmp1.columns.values[2] += ("_" + file_list[2] + "_" + file_list[3])
            data_new = pd.concat([data_all, tmp1], axis=1)

            data_new.to_csv("/Users/bg/PycharmProjects/combine_to_df/output/rnd_all_pe.csv")


def combine_dfs():
    data_lexdec = pd.read_csv("/Users/bg/PycharmProjects/combine_to_df/output/lexdec_most_freq_all_pe.csv")
    data_all = pd.read_csv("/Users/bg/PycharmProjects/combine_to_df/output/rnd_all_pe.csv")
    data_all = data_all.iloc[:, 1:]
    merged_df = pd.merge(data_lexdec, data_all, on='string', how='left').drop_duplicates()
    # data_lexdec.join(other=data_all, on="string")
    # merged_df
    print(merged_df['category'].value_counts())
    merged_df.to_csv("/Users/bg/PycharmProjects/combine_to_df/output/lexdec_most_freq_and_rnd_all_pe.csv")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # make_df_from_files()
    #make_df_from_files_rnd()
    combine_dfs()
