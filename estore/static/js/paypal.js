var total = '{{order.get_cart_total}}'
        // Render the PayPal button into #paypal-button-container
        paypal.Buttons({

        	style: {
                color:  'gold',
                shape:  'rect',
            },

            // Set up the transaction
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value:parseFloat(total).toFixed(2)
                        }
                    }]
                });
            },

            // Finalize the transaction
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(details) {
                    // Show a success message to the buyer
					alert('Transaction completed by ' + details.payer.name.given_name + '!');
                    submitFormData()
                });
            }

        }).render('#paypal-button-container');