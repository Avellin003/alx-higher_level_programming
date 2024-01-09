#!/usr/bin/node
const i = process.argv.length - 2;
if (i === 0)
{
	console.log('No argument');
}
else if (i === 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
