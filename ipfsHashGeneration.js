const shell = require('shelljs');
const fs = require('fs');

const hashGen = async organ => {
    //const fileName = (await makeFileName()) + '.json';
    const fileName = 'data.json';
    await fs.writeFileSync(fileName, JSON.stringify(organ, null, 2), 'utf-8');
    const { stdout, stderr, code } = await shell.exec(
        `${__dirname}/script.sh ${fileName}`
    );
    //console.log(stdout);
    var result = stdout.split(' ');
    return result[1];
};

module.exports = {
    hashGen
};
