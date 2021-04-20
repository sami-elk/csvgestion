matplotlib.use("Agg")

# Declaration de la fonction qui import le fichier
def importFile(nom_fichier):
    df = pd.read_csv(nom_fichier)
    return df

# Declaration de la fonction qui lit le fichier
def afficheFile(file):
    return file.head(file.shape[0])
#déclaration de la fonction qui détermine les types des données
def datatype(file):
    ty=file.dtypes
    return ty
#ghjkl
def Fichier_final(file):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    path=filedialog.askdirectory(master=root)+'/Fichier.csv'   
    with open(path, 'w', newline='') as csvfile:
        fieldnames=[]
        testhh={}
        for i in range(0,len(file.columns)):
            fieldnames.append(file.columns[i])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0,file.shape[0]):
            for j in range(0,len(file.columns)):
                testhh[file.columns[j]] = file[file.columns[j]][i]
            writer.writerow(testhh)
#l'appel du fichier html/css 
def st_page(calc_html,width=700,height=500):
    calc_file=codecs.open(calc_html,'r')
    page=calc_file.read()
    stc.html(page,width=width,height=height,scrolling=False)
#MAIN
file=0
