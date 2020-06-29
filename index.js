const Discord = require('discord.js');
const bot = new Discord.Client();
const token = "NzI3MjA3NTA1MjM4Njg3ODE2.Xvoe0Q.7D-EQ_G9g9EPiHaGKPhHQTMNSgM"

bot.on('ready', () => {
    console.log('This bot is online')

})

bot.on('message', msg => {
    if(msg.content == "Hello") { 
        msg.reply('HELLO WORLD') 
    }
})

bot.login(token);
