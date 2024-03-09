const { exec } = require('child_process');

const startServer = () => {
  exec('http-server /home/pyslarash/Documents/code/aiartonacob/api -p 5001 --show-dir', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error starting http-server: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`http-server stderr: ${stderr}`);
      return;
    }
    console.log(`http-server stdout: ${stdout}`);
  });
};

startServer();
