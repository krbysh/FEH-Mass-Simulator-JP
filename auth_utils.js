function requestAccessToken() {
    var JWT = doSign();
    var XHR = new XMLHttpRequest();
    var urlEncodedData = "";
    var urlEncodedDataPairs = [];

    urlEncodedDataPairs.push("grant_type=" + encodeURIComponent("urn:ietf:params:oauth:grant-type:jwt-bearer"));
    urlEncodedDataPairs.push("assertion=" + encodeURIComponent(JWT));
    urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+');


    function writeResponse(jsonResp, rawResp) {
        document.myform.accessToken.value = rawResp;
    }

    var request = gapi.client.request({
            'path': '/oauth2/v3/token',
            'method': 'POST',
            'headers': {"Content-Type": "application/x-www-form-urlencoded"},
            'body': urlEncodedData
    });
    request.execute(writeResponse);

}

//JWS signature algorithm: SHA256withRSA with PKCS#8 plain private key(z4)
function doSign() {
    var sClaim = JSON.stringify(getClaim());

    var pHeader = {'alg': "RS256", 'typ': 'JWT'};
    var sHeader = JSON.stringify(pHeader);

    var key = myPrivateKeyPkcs8Pem;

    var JWT = '';
    JWT = KJUR.jws.JWS.sign(null, sHeader, sClaim, key);
    document.myform.jwt.value = JWT;

    return JWT;
}

function getClaim() {
    var r = {};
    r.iss = "<myserviceaccount>@developer.gserviceaccount.com";
    r.scope = "https://www.googleapis.com/auth/drive.file";
    r.aud = "https://www.googleapis.com/oauth2/v3/token";
    r.exp = KJUR.jws.IntDate.get("now + 1hour");
    r.iat = KJUR.jws.IntDate.get("now");
    //http://kjur.github.io/jsjws/api/symbols/KJUR.jws.IntDate.html#.get

    return r;
}

//skipped my private key
var myPrivateKeyPkcs8Pem = "" +
"-----BEGIN PRIVATE KEY-----\n" +
"MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCvhIw/cxJ6QS6Z\nVVUmmE1FVzdZUL1jG1p/ZWd3NkJ8zKVIWpJatsEIIBHzy0WDT2gv46J8cWldxsug\n+XvuoDDID6HIXedBy/YuDCbtIxdX8QYtqowwqpOUYdrKN4PzC5Gb8a2XLbTtemw3\nBGHwrToYkTbgmtnPkT/B/3L6vVS6ziIcfmv7Mkd+1n0W3hN0RQGSGxPTB4c6jzrH\nMwfwJ3dlPLMxQV7jsgkSDSwBq054QsPiQXrWVD5RpQ/IFAfKt1pFRLNkPXZu0nrq\noQ9dOF34eDhIttXm3394eNjnb1Vu0VI8B9Locr7lr8wwiAu1UaFw0mcMug3G/LDd\nbbfzraTnAgMBAAECggEAQ+EFolY8+6XwwSEkzMfS/nGj+LlGfSkrfyB2+r4zyXMV\nqt1IQ6fxEFTizH+9EvLnTroA8ZKk1r0WrFtACEHQi9ar0UMruCEKxLUzaruLABo5\nMvkFvZ6Cc7zCcjk1IQ5E0mQNp+1nzv3tEvvxarR7xtuGNyf7+4/ncf36eCk3twRz\n19GudFRmwcLOv52K+VathvUZJ6elypWfo9WJQrgbZZTz4bxDi0/LvUi4Leo8T2z9\newMa65vVl80YEWJKEqWchYFi/rjAHRZiwYR7cjjPQcD1VKyjjOn+/PIXanq3KgeN\nVGQS9VLg7XfgPwceJ0joaox8bbRaCul7YvdK1YrKxQKBgQDmlwUQyljPNDQOXPrO\ndU42JCzlzGDFhs8jGFPYPJV0KqPO/dhJ8Qho00/TGKkxwQoggt/PkZXLpWecBMDV\naNpZCnqBPKIOiI6PFA7KgNBjGKCCAGCGdGL+oaSdL1oRHD50jbWbQc1fIGIMmUZC\nxfr07XaMC8chqtOw8+obRhtGYwKBgQDC2+7urpX/jfvAGIfetx+SRRKtLryjxbRn\ncQFIzGNu8qiXxi7irrQeqTlBJcnQtBO0+42gbwWNhLHudT157yqMjGrQCxNyJJcE\n17xNXlXVtZNFUsGLTT2YBneCAdMpzSuZyqYT3HZvWNuJK7lsJgGlhimkOizOJkaF\nKEa5RNbcrQKBgFfpl9rQ6o8E3hvjwxNXkdv+asep5fMo9Gvy6HR2lJxXbWCLUxzN\nsmEUv0hCDK+VY2EFxIKEhNHBXAEVptc2RJjR7+a50SctVPyjrwfxmIFPcFJgBmz8\njol54yKyXOpNFFqndGee7MeptvgKr8jhZk5fAmVeUCs7z72VINoJHnj1AoGASOVI\nBChx2tF93YYPxiSRfgGzE/CJB2ddrtjalyZHCGlk4qp0Pb8HiPTbg2CkmBvVx33X\npK4D0MZUXhWj8uqi60NYbg3Gr4u6p0ghnHvu9mzf9C4aU4eIxEefC5atLVUgu37R\nFFsEP3FpZ25hBnFNamO/Tj2pJ1GwTf4cPxDepF0CgYADrwIQcu3BfoW4fZQH+eVM\nx91c9unM1R0ECNdMQHyMjmAHgoWghGncdFZoix/Jj5S7wdfYbatTOUdjL8clYxWA\nSBkNYhz14royS6PDfhJGYHdItSS1sWUxWLlSLFCWP0LE8Y9gu4LniLu7ppx3DumS\nd2Hvei4sESooSPu+T8gwsQ==\n" + 
"-----END PRIVATE KEY-----\n";
