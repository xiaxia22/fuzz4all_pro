# Class KeyStoreLoginModule

**Source:** `jdk.security.auth\com\sun\security\auth\module\KeyStoreLoginModule.html`

### Class Description

```java
public class
KeyStoreLoginModule

extends
Object

implements
LoginModule
```

Provides a JAAS login module that prompts for a key store alias and
populates the subject with the alias's principal and credentials. Stores
an

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's principals,
the alias's certificate path in the subject's public credentials, and a

X500PrivateCredential

whose certificate is the first
certificate in the alias's certificate path and whose private key is the
alias's private key in the subject's private credentials.

Recognizes the following options in the configuration file:

**keyStoreURL:** A URL that specifies the location of the key store. Defaults to
a URL pointing to the .keystore file in the directory specified by the

user.home

system property. The input stream from this
URL is passed to the

KeyStore.load

method.
"NONE" may be specified if a

null

stream must be
passed to the

KeyStore.load

method.
"NONE" should be specified if the KeyStore resides
on a hardware token device, for example.
**keyStoreType:** The key store type. If not specified, defaults to the result of
calling

KeyStore.getDefaultType()

.
If the type is "PKCS11", then keyStoreURL must be "NONE"
and privateKeyPasswordURL must not be specified.
**keyStoreProvider:** The key store provider. If not specified, uses the standard search
order to find the provider.
**keyStoreAlias:** The alias in the key store to login as. Required when no callback
handler is provided. No default value.
**keyStorePasswordURL:** A URL that specifies the location of the key store password. Required
when no callback handler is provided and

protected

is false.
No default value.
**privateKeyPasswordURL:** A URL that specifies the location of the specific private key password
needed to access the private key for this alias.
The keystore password
is used if this value is needed and not specified.
**protected:** This value should be set to "true" if the KeyStore
has a separate, protected authentication path
(for example, a dedicated PIN-pad attached to a smart card).
Defaults to "false". If "true" keyStorePasswordURL and
privateKeyPasswordURL must not be specified.

**All Implemented Interfaces:** LoginModule

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyStoreLoginModule()

*No description found.*

---

### Method Details

#### public void initialize​(
Subject
subject,

CallbackHandler
callbackHandler,

Map
<
String
,​?> sharedState,

Map
<
String
,​?> options)

Initialize this

LoginModule

.

**Specified by:**
- initialize

in interface

LoginModule

**Parameters:**
- subject

- the

Subject

to be authenticated.
- callbackHandler

- a

CallbackHandler

for communicating
with the end user (prompting for usernames and
passwords, for example),
which may be

null

.
- sharedState

- shared

LoginModule

state.
- options

- options specified in the login

Configuration

for this particular

LoginModule

.

---

#### public boolean login()
throws
LoginException

Authenticate the user.

Get the Keystore alias and relevant passwords.
Retrieve the alias's principal and credentials from the Keystore.

**Specified by:**
- login

in interface

LoginModule

**Returns:**
- true in all cases (this

LoginModule

should not be ignored).

**Throws:**
- FailedLoginException

- if the authentication fails.
- LoginException

- if the authentication fails

---

#### public boolean commit()
throws
LoginException

Abstract method to commit the authentication process (phase 2).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:**
- commit

in interface

LoginModule

**Returns:**
- true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.

**Throws:**
- LoginException

- if the commit fails

---

#### public boolean abort()
throws
LoginException

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:**
- abort

in interface

LoginModule

**Returns:**
- false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.

**Throws:**
- LoginException

- if the abort fails.

---

#### public boolean logout()
throws
LoginException

Logout a user.

This method removes the Principals, public credentials and the
private credentials that were added by the

commit

method.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:**
- logout

in interface

LoginModule

**Returns:**
- true in all cases since this

LoginModule

should not be ignored.

**Throws:**
- LoginException

- if the logout fails.

---

### Additional Sections

#### Class KeyStoreLoginModule

java.lang.Object

- com.sun.security.auth.module.KeyStoreLoginModule

com.sun.security.auth.module.KeyStoreLoginModule

**All Implemented Interfaces:** LoginModule

```java
public class
KeyStoreLoginModule

extends
Object

implements
LoginModule
```

Provides a JAAS login module that prompts for a key store alias and
populates the subject with the alias's principal and credentials. Stores
an

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's principals,
the alias's certificate path in the subject's public credentials, and a

X500PrivateCredential

whose certificate is the first
certificate in the alias's certificate path and whose private key is the
alias's private key in the subject's private credentials.

Recognizes the following options in the configuration file:

**keyStoreURL:** A URL that specifies the location of the key store. Defaults to
a URL pointing to the .keystore file in the directory specified by the

user.home

system property. The input stream from this
URL is passed to the

KeyStore.load

method.
"NONE" may be specified if a

null

stream must be
passed to the

KeyStore.load

method.
"NONE" should be specified if the KeyStore resides
on a hardware token device, for example.
**keyStoreType:** The key store type. If not specified, defaults to the result of
calling

KeyStore.getDefaultType()

.
If the type is "PKCS11", then keyStoreURL must be "NONE"
and privateKeyPasswordURL must not be specified.
**keyStoreProvider:** The key store provider. If not specified, uses the standard search
order to find the provider.
**keyStoreAlias:** The alias in the key store to login as. Required when no callback
handler is provided. No default value.
**keyStorePasswordURL:** A URL that specifies the location of the key store password. Required
when no callback handler is provided and

protected

is false.
No default value.
**privateKeyPasswordURL:** A URL that specifies the location of the specific private key password
needed to access the private key for this alias.
The keystore password
is used if this value is needed and not specified.
**protected:** This value should be set to "true" if the KeyStore
has a separate, protected authentication path
(for example, a dedicated PIN-pad attached to a smart card).
Defaults to "false". If "true" keyStorePasswordURL and
privateKeyPasswordURL must not be specified.

public class

KeyStoreLoginModule

extends

Object

implements

LoginModule

Provides a JAAS login module that prompts for a key store alias and
populates the subject with the alias's principal and credentials. Stores
an

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's principals,
the alias's certificate path in the subject's public credentials, and a

X500PrivateCredential

whose certificate is the first
certificate in the alias's certificate path and whose private key is the
alias's private key in the subject's private credentials.

Recognizes the following options in the configuration file:

**keyStoreURL:** A URL that specifies the location of the key store. Defaults to
a URL pointing to the .keystore file in the directory specified by the

user.home

system property. The input stream from this
URL is passed to the

KeyStore.load

method.
"NONE" may be specified if a

null

stream must be
passed to the

KeyStore.load

method.
"NONE" should be specified if the KeyStore resides
on a hardware token device, for example.
**keyStoreType:** The key store type. If not specified, defaults to the result of
calling

KeyStore.getDefaultType()

.
If the type is "PKCS11", then keyStoreURL must be "NONE"
and privateKeyPasswordURL must not be specified.
**keyStoreProvider:** The key store provider. If not specified, uses the standard search
order to find the provider.
**keyStoreAlias:** The alias in the key store to login as. Required when no callback
handler is provided. No default value.
**keyStorePasswordURL:** A URL that specifies the location of the key store password. Required
when no callback handler is provided and

protected

is false.
No default value.
**privateKeyPasswordURL:** A URL that specifies the location of the specific private key password
needed to access the private key for this alias.
The keystore password
is used if this value is needed and not specified.
**protected:** This value should be set to "true" if the KeyStore
has a separate, protected authentication path
(for example, a dedicated PIN-pad attached to a smart card).
Defaults to "false". If "true" keyStorePasswordURL and
privateKeyPasswordURL must not be specified.

Recognizes the following options in the configuration file:

**keyStoreURL:** A URL that specifies the location of the key store. Defaults to
a URL pointing to the .keystore file in the directory specified by the

user.home

system property. The input stream from this
URL is passed to the

KeyStore.load

method.
"NONE" may be specified if a

null

stream must be
passed to the

KeyStore.load

method.
"NONE" should be specified if the KeyStore resides
on a hardware token device, for example.
**keyStoreType:** The key store type. If not specified, defaults to the result of
calling

KeyStore.getDefaultType()

.
If the type is "PKCS11", then keyStoreURL must be "NONE"
and privateKeyPasswordURL must not be specified.
**keyStoreProvider:** The key store provider. If not specified, uses the standard search
order to find the provider.
**keyStoreAlias:** The alias in the key store to login as. Required when no callback
handler is provided. No default value.
**keyStorePasswordURL:** A URL that specifies the location of the key store password. Required
when no callback handler is provided and

protected

is false.
No default value.
**privateKeyPasswordURL:** A URL that specifies the location of the specific private key password
needed to access the private key for this alias.
The keystore password
is used if this value is needed and not specified.
**protected:** This value should be set to "true" if the KeyStore
has a separate, protected authentication path
(for example, a dedicated PIN-pad attached to a smart card).
Defaults to "false". If "true" keyStorePasswordURL and
privateKeyPasswordURL must not be specified.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyStoreLoginModule

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

abort

()

This method is called if the LoginContext's
overall authentication failed.

boolean

commit

()

Abstract method to commit the authentication process (phase 2).

void

initialize

​(

Subject

subject,

CallbackHandler

callbackHandler,

Map

<

String

,​?> sharedState,

Map

<

String

,​?> options)

Initialize this

LoginModule

.

boolean

login

()

Authenticate the user.

boolean

logout

()

Logout a user.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

KeyStoreLoginModule

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

abort

()

This method is called if the LoginContext's
overall authentication failed.

boolean

commit

()

Abstract method to commit the authentication process (phase 2).

void

initialize

​(

Subject

subject,

CallbackHandler

callbackHandler,

Map

<

String

,​?> sharedState,

Map

<

String

,​?> options)

Initialize this

LoginModule

.

boolean

login

()

Authenticate the user.

boolean

logout

()

Logout a user.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

This method is called if the LoginContext's
overall authentication failed.

Abstract method to commit the authentication process (phase 2).

Initialize this

LoginModule

.

Authenticate the user.

Logout a user.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KeyStoreLoginModule

```java
public KeyStoreLoginModule()
```

============ METHOD DETAIL ==========

- Method Detail

- initialize

```java
public void initialize​(
Subject
subject,

CallbackHandler
callbackHandler,

Map
<
String
,​?> sharedState,

Map
<
String
,​?> options)
```

Initialize this

LoginModule

.

**Specified by:** initialize

in interface

LoginModule
**Parameters:** subject

- the

Subject

to be authenticated.
**Parameters:** callbackHandler

- a

CallbackHandler

for communicating
with the end user (prompting for usernames and
passwords, for example),
which may be

null

.
**Parameters:** sharedState

- shared

LoginModule

state.
**Parameters:** options

- options specified in the login

Configuration

for this particular

LoginModule

.

- login

```java
public boolean login()
throws
LoginException
```

Authenticate the user.

Get the Keystore alias and relevant passwords.
Retrieve the alias's principal and credentials from the Keystore.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** FailedLoginException

- if the authentication fails.
**Throws:** LoginException

- if the authentication fails

- commit

```java
public boolean commit()
throws
LoginException
```

Abstract method to commit the authentication process (phase 2).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails

- abort

```java
public boolean abort()
throws
LoginException
```

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:** abort

in interface

LoginModule
**Returns:** false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.
**Throws:** LoginException

- if the abort fails.

- logout

```java
public boolean logout()
throws
LoginException
```

Logout a user.

This method removes the Principals, public credentials and the
private credentials that were added by the

commit

method.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases since this

LoginModule

should not be ignored.
**Throws:** LoginException

- if the logout fails.

Constructor Detail

- KeyStoreLoginModule

```java
public KeyStoreLoginModule()
```

---

#### Constructor Detail

KeyStoreLoginModule

```java
public KeyStoreLoginModule()
```

---

#### KeyStoreLoginModule

public KeyStoreLoginModule()

Method Detail

- initialize

```java
public void initialize​(
Subject
subject,

CallbackHandler
callbackHandler,

Map
<
String
,​?> sharedState,

Map
<
String
,​?> options)
```

Initialize this

LoginModule

.

**Specified by:** initialize

in interface

LoginModule
**Parameters:** subject

- the

Subject

to be authenticated.
**Parameters:** callbackHandler

- a

CallbackHandler

for communicating
with the end user (prompting for usernames and
passwords, for example),
which may be

null

.
**Parameters:** sharedState

- shared

LoginModule

state.
**Parameters:** options

- options specified in the login

Configuration

for this particular

LoginModule

.

- login

```java
public boolean login()
throws
LoginException
```

Authenticate the user.

Get the Keystore alias and relevant passwords.
Retrieve the alias's principal and credentials from the Keystore.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** FailedLoginException

- if the authentication fails.
**Throws:** LoginException

- if the authentication fails

- commit

```java
public boolean commit()
throws
LoginException
```

Abstract method to commit the authentication process (phase 2).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails

- abort

```java
public boolean abort()
throws
LoginException
```

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:** abort

in interface

LoginModule
**Returns:** false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.
**Throws:** LoginException

- if the abort fails.

- logout

```java
public boolean logout()
throws
LoginException
```

Logout a user.

This method removes the Principals, public credentials and the
private credentials that were added by the

commit

method.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases since this

LoginModule

should not be ignored.
**Throws:** LoginException

- if the logout fails.

---

#### Method Detail

initialize

```java
public void initialize​(
Subject
subject,

CallbackHandler
callbackHandler,

Map
<
String
,​?> sharedState,

Map
<
String
,​?> options)
```

Initialize this

LoginModule

.

**Specified by:** initialize

in interface

LoginModule
**Parameters:** subject

- the

Subject

to be authenticated.
**Parameters:** callbackHandler

- a

CallbackHandler

for communicating
with the end user (prompting for usernames and
passwords, for example),
which may be

null

.
**Parameters:** sharedState

- shared

LoginModule

state.
**Parameters:** options

- options specified in the login

Configuration

for this particular

LoginModule

.

---

#### initialize

public void initialize​(

Subject

subject,

CallbackHandler

callbackHandler,

Map

<

String

,​?> sharedState,

Map

<

String

,​?> options)

Initialize this

LoginModule

.

login

```java
public boolean login()
throws
LoginException
```

Authenticate the user.

Get the Keystore alias and relevant passwords.
Retrieve the alias's principal and credentials from the Keystore.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** FailedLoginException

- if the authentication fails.
**Throws:** LoginException

- if the authentication fails

---

#### login

public boolean login()
throws

LoginException

Authenticate the user.

Get the Keystore alias and relevant passwords.
Retrieve the alias's principal and credentials from the Keystore.

Get the Keystore alias and relevant passwords.
Retrieve the alias's principal and credentials from the Keystore.

commit

```java
public boolean commit()
throws
LoginException
```

Abstract method to commit the authentication process (phase 2).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails

---

#### commit

public boolean commit()
throws

LoginException

Abstract method to commit the authentication process (phase 2).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

X500Principal

for the subject distinguished name of the
first certificate in the alias's credentials in the subject's
principals,the alias's certificate path in the subject's public
credentials, and a

X500PrivateCredential

whose certificate
is the first certificate in the alias's certificate path and whose
private key is the alias's private key in the subject's private
credentials. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

abort

```java
public boolean abort()
throws
LoginException
```

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:** abort

in interface

LoginModule
**Returns:** false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.
**Throws:** LoginException

- if the abort fails.

---

#### abort

public boolean abort()
throws

LoginException

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

logout

```java
public boolean logout()
throws
LoginException
```

Logout a user.

This method removes the Principals, public credentials and the
private credentials that were added by the

commit

method.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases since this

LoginModule

should not be ignored.
**Throws:** LoginException

- if the logout fails.

---

#### logout

public boolean logout()
throws

LoginException

Logout a user.

This method removes the Principals, public credentials and the
private credentials that were added by the

commit

method.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

This method removes the Principals, public credentials and the
private credentials that were added by the

commit

method.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

If the loaded KeyStore's provider extends

java.security.AuthProvider

,
then the provider's

logout

method is invoked.

---

