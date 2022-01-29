# Certomancer-based dummy CSC server implementation

## Overview

This package contains a minimal implementation of the Cloud Signature
Consortium (CSC) API for remote signing. It's intended for use in
integration tests and demonstrations.
Most of the heavy lifting is actually done by
[Certomancer](https://github.com/MatthiasValvekens/certomancer). This package
merely wraps calls to Certomancer in an `aiohttp`-based web interface that
exposes (a subset of) the CSC API.

This is a **testing tool**, and it omits all sorts of essential security features:

 - Requests are not authenticated
 - No SAD replay prevention of any sort, other than the standard hash pinning
   supported by the CSC protocol
 - All keys in the Certomancer config can be used to sign hashes in CSC calls

**It goes without saying that you should _never_ use this implementation, or any
derivative thereof, with production keys.**


## Missing features

Besides most authentication-related endpoints, the following CSC features are also missing:

 - `signatures/timestamp`
 - `credentials/extendTransaction`

These may be implemented in the future.

The other obvious missing feature is "anything resembling a decent user interface".
This code was essentially isolated from
[pyHanko's](https://github.com/MatthiasValvekens/pyHanko) integration tests in the hope that
it might be useful for others to play around with, and the primitive CLI reflects that.


## Invocation

This is the command syntax. All parameters are required.

```bash
certomancer-csc CERTOMANCER_CONFIG PORT SCAL
```

The meaning of the parameters is as follows:

 - `CERTOMANCER_CONFIG` is the path to your Certomancer config file, usually called
   `certomancer.yml`
 - `PORT` is the port on which you want the dummy server to listen
 - `SCAL` indicates whether SAD data is required to be bound to hashes
   (`1`=no, `2`=yes) &mdash; see the CSC specification for details.
 
The credentials exposed in the CSC API are in one-to-one correspondence with
certificates in Certomancer (assuming Certomancer has access to all the private keys).
The naming convention for credentials is `<arch>/<cert-label>`, where `<arch>` is the
name of the Certomancer PKI architecture you're trying to access, and `<cert-label>`
is the label of the certificate that will be treated as the signer's certificate.
Example: `testing-ca/signer1` would access the certificate `signer1` in the
architecture labelled `testing-ca`. Signatures will be produced by the corresponding
private key.

Again, note that all credentials are always available without any form of authentication,
although the caller is still required to go through the motions of requesting a SAD token
before any signatures will be returned.

## Example usage

See here:

 - [the workflow code](https://github.com/MatthiasValvekens/pyHanko/blob/master/.github/workflows/live-integration-tests.yml)
   for pyHanko's "live" integration test setup
 - [the dummy client implementation](https://github.com/MatthiasValvekens/pyHanko/blob/master/pyhanko_tests/csc_utils/csc_dummy_client.py)
   used in pyHanko's tests

## License

MIT license.