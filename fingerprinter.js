function getFingerprint() {
    return 'TODO';
}

async function uploadFingerprint(fingerprint, cookieId) {
    if (!cookieId) return;
    if (!fingerprint) return;

    await fetch('/', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cookieId, fingerprint });
    });
}

uploadFingerprint(getFingerprint(), document.cookie[])