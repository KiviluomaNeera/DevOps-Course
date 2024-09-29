const express = require('express');
const os = require('os');
const { execSync } = require('child_process');

const app = express();

// Function to get container info
const getContainerInfo = () => {
    const ipAddress = Object.values(os.networkInterfaces())
        .flat()
        .find((iface) => iface.family === 'IPv4' && !iface.internal).address;

    const processes = execSync('ps -ax').toString();
    const diskSpace = execSync('df -h /').toString();
    const uptime = execSync('uptime -p').toString();

    return {
        ip_address: ipAddress,
        processes: processes,
        disk_space: diskSpace,
        uptime: uptime
    };
};

// HTTP route for getting container info
app.get('/info', (req, res) => {
    res.json(getContainerInfo());
});

// HTTP route for default home page (optional)
app.get('/', (req, res) => {
    res.send('Welcome to Service 2! Use /info to get container information.');
});

app.listen(3000, () => {
    console.log('Service 2 running on port 3000');
});
