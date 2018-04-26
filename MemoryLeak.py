#关于内存泄漏
for m in range(len(EachAA)):
                #Establish axis first
                EachAA[m].EstablishCoordinate()
                for n in range(len(EachAA)):
                    if(m == n):
                        continue
                    else:
                        dis = EachAA[m].DistanceBetweenAA(EachAA[n].center)
                        if(dis <= 10):#If the distance between two amino acid less than 10, we believe the two amino acid have interaction
                            #print EachAA[m].ChangeCoordinate(EachAA[n].center)   
                            rho,theta,phi = EachAA[m].ChangeCoordinate(EachAA[n].center)
                            theta = min(int(np.floor(theta*20/np.pi)),19)
                            phi = min(int(np.floor(phi*10/np.pi) + 10),19)
                            #Check the energy matrix and get the energy   
                            E += cdDict[EachAA[m].name][EachAA[n].name][theta][phi] / rho
