module.exports = (robot) ->
    
        
		fs = require("fs");
		path = "/home/anuja/hubot/1.txt";
		robot.respond /mycroft/, (msg) ->
			data = msg.message;
			fs.writeFile(path, data)
			
			
			start = new Date().getTime()
			continue while new Date().getTime() - start < 5000
			
			path2= "/home/anuja/hubot/2.txt";
			foo= fs.readFileSync path2, 'utf8'
			msg.send foo;
		
