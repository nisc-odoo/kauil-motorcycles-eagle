/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.s_odometer = publicWidget.Widget.extend({
    selector: '.odometer-dis',
    /**
     * @override
     */
    start() {
        console.log("DOES THIS WORK?");
        let odometerRow = this.el.querySelector('#odometer-row-dis')

        if(odometerRow){
            console.log("starting query");
            this._rpc({
                route: '/odometer/',
                params:{"id":"test"}
            }).then(data=>{
                console.log("got data");
                let html = ''
                let total = 0
                data.forEach(bike => {
                    total += bike.current_mileage
                    console.log(bike)
                    console.log(total)
                })
                html+=`<div class="col-lg-3 mb-5">
                            <div class="d-flex align-items-center">
                                <div>
                                    <h1 class="mb-0">${total}</h1>
                                </div>
                            </div>
                        </div>`
                odometerRow.innerHTML = html
            })
        }else{
            console.log("could not select element row")
        }
    },

        
});

export default publicWidget.registry.s_odometer;

