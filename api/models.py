from django.db import models

class Proprietaire(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    cni = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)

class Locataire(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    cni = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)

class Logement(models.Model):
    id_logement = models.CharField(max_length=30, primary_key=True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, null=True, blank=True, on_delete=models.SET_NULL)
    adresse = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)
    type_logement = models.CharField(max_length=30)
    nombre_piece = models.IntegerField()
    statut = models.CharField(max_length=30)

class Contrat(models.Model):
    id_contrat = models.CharField(max_length=30, primary_key=True)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    type_contrat = models.CharField(max_length=30)

class Paiement(models.Model):
    ref = models.CharField(max_length=30, primary_key=True)
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE)
    date_paiement = models.DateField()
    montant = models.IntegerField()
    moyen_paiement = models.CharField(max_length=30)
