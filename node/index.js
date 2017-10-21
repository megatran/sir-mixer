'use strict';

const Alexa = require('alexa-sdk');

const APP_ID = undefined;  // TODO replace with your app ID (OPTIONAL).

const COMMAND_PORT = 1337;
const SERVER_IP = '54.152.117.238';
const net = require('net');
const DRINK_CODES = {
                     'water'    : 'a',
                     'coke'     : 'b',
                     'sprite'   : 'c',
                     'lemonade' : 'd'
                    };

const handlers = {
    'MakeDrink' : function ()
    {
        console.log('In MakeDrink intent handler');
        var drinkSlot = this.event.request.intent.slots.drink;
        if (drinkSlot.value == undefined)
        {
            console.log('no drink defined for this event');
            this.emit(':delegate', this.event.request.intent);
        }
        else {
            console.log('the drink is ' + drinkSlot.value);
            // transmit the command via TCP to the EC2 server
            var socket = new net.Socket();
            console.log('initialized socket');
            var handlerTest = this;
            socket.connect(COMMAND_PORT, SERVER_IP, function()
            {
                console.log('made connection to server');
                socket.write(DRINK_CODES[drinkSlot.value],
                    function()
                    {
                        console.log('wrote ' + DRINK_CODES[drinkSlot.value] + ' to the socket, destroying socket');
                        socket.destroy();
                        handlerTest.emit(':tell', 'Sure thing. One ' + drinkSlot.value + ' coming right up.');
                    });
            });
        }

    },
};

exports.handler = function (event, context) {
    console.log(event)
    const alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    // To enable string internationalization (i18n) features, set a resources object.
    alexa.registerHandlers(handlers);
    alexa.execute();
};
