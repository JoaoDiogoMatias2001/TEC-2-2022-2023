import ROOT
ficheiro = ROOT.TFile.Open("teste.root","READ")

browser = ROOT.TBrowser()
tree = ficheiro.Get("eventos")
tree.Scan()

entries = tree.GetEntries()
print(entries)

histograma = tree.Draw('Nep')
tree.SaveAs('hist1.png')
