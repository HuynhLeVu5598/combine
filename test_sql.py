                                if values[f'{model1.names[i1]}_1'] == False:
                                    if label_name == model1.names[i1]:
                                        table1.drop(item, axis=0, inplace=True)
                                        area_remove1.append(item)
            

                                if values[f'{model2.names[i2]}_2'] == False:
                                    if label_name == model2.names[i2]:
                                        table2.drop(item, axis=0, inplace=True)
                                        area_remove2.append(item)


                                if values[f'{model3.names[i3]}_3'] == False:
                                    if label_name == model3.names[i3]:
                                        table3.drop(item, axis=0, inplace=True)
                                        area_remove3.append(item)



                                if values[f'{model4.names[i4]}_4'] == False:
                                    if label_name == model4.names[i4]:
                                        table4.drop(item, axis=0, inplace=True)
                                        area_remove4.append(item)
