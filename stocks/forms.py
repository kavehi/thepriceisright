from django import forms

from models import ParentOrder


class ParentOrderForm(forms.ModelForm):

	BUY_OR_SELL_CHOICE = (
    	(True, 'Sell'),
	)

	STOCK_CHOICE = (
    	('ACME ETF', 'ACME ETF'),
	)

	is_sell = forms.ChoiceField(label="Buy or Sell?", choices=BUY_OR_SELL_CHOICE, required=True, 
		widget=forms.Select(attrs={'class': 'form-control'}))
	quantity = forms.IntegerField(label='Quantity', required=True, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}))
	stock_type = forms.ChoiceField(label="Stock Type", choices=STOCK_CHOICE, required=True, 
		widget=forms.Select(attrs={'class': 'form-control'}))


	class Meta:
		model = ParentOrder
		fields = ('is_sell', 'quantity', 'stock_type')
