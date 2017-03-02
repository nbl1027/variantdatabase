from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from .models import *
from .forms import *
from snps.resultentry import *

# Create your views here.

#def home(request):
#    return HttpResponse('Hello World')

def home(request):
    return render_to_response('snps/home.html')

def success(request):
    return render_to_response('snps/success.html')

def variants(request):
    variants = Variant.objects.all()
    return render_to_response('snps/variants.html')

def handle_uploaded_file(f, chrom, gene):
    variants = []
    lines = f.readlines()
    for row in lines:
            yoy = row.strip().split('\t')
            variants.append(yoy)
    i, created = Institution.objects.get_or_create(name = 'BALaboratories', location = 'Planet Cool', contactname = 'LL Cool J', contactnumber = 12345678, contactemail = 'LLCoolJ@BAL.com')
    for row in variants:
	    if row[0] == 'Name':
                continue
            print row
            first, last = row[0].split(' ')
            age = int(row[1])
	    inst = 2 
	    p, created = Patient.objects.get_or_create( 
                firstname = first,
                secondname = last,
                age = age, 
                institutionid  = i.institutionid)
            stype = row[3]
            sequencer = row[4] 
            s, created = Samples.objects.get_or_create(patientid = p.patientid, sequencer = sequencer, sampletype = stype)
            cdna = row[5]
            gdna = row[7]
            protein = row[6]
	    v, created = Variant.objects.get_or_create(cdna = cdna, gdna = gdna, protein = protein, chromosome = chrom, gene = gene)
            v2p, created = Sample2Variant.objects.get_or_create(variantid = v.variantid, sampleid = s.sampleid)       
    return 

def upload_file(request):
    print request.__dict__.keys()
    print request.POST.get('chromosome')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['results'], request.POST.get('chromosome'), request.POST.get('gene'))
            return render(request,'snps/success.html')
        else:
            form = UploadFileForm()
            return render_to_response('snps/success.html')
    else:
        form = UploadFileForm()
	return render(request, 'upload.html', {'form':form})


   

#def chromosome_home(request):
 #   return render_to_response("snps/chromosome_home.html", {'chromosome_list': Chromosome.objects.all()})

#def chromosome_details(request, pk):
 #   chromosome = get_object_or_404(Chromosome, pk=pk)
  #  return render(request, 'snps/chromosome_details.html', {'chromosome': chromosome})