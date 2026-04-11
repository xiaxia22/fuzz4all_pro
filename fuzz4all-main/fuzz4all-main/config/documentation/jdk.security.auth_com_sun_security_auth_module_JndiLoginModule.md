# Class JndiLoginModule

**Source:** `jdk.security.auth\com\sun\security\auth\module\JndiLoginModule.html`

### Class Description

```java
public class
JndiLoginModule

extends
Object

implements
LoginModule
```

The module prompts for a username and password
and then verifies the password against the password stored in
a directory service configured under JNDI.

This

LoginModule

interoperates with
any conformant JNDI service provider. To direct this

LoginModule

to use a specific JNDI service provider,
two options must be specified in the login

Configuration

for this

LoginModule

.

```java
user.provider.url=
name_service_url

group.provider.url=
name_service_url
```

name_service_url

specifies
the directory service and path where this

LoginModule

can access the relevant user and group information. Because this

LoginModule

only performs one-level searches to
find the relevant user information, the

URL

must point to a directory one level above where the user and group
information is stored in the directory service.
For example, to instruct this

LoginModule

to contact a NIS server, the following URLs must be specified:

```java
user.provider.url="nis://
NISServerHostName
/
NISDomain
/user"
group.provider.url="nis://
NISServerHostName
/
NISDomain
/system/group"
```

NISServerHostName

specifies the server host name of the
NIS server (for example,

nis.sun.com

, and

NISDomain

specifies the domain for that NIS server (for example,

jaas.sun.com

.
To contact an LDAP server, the following URLs must be specified:

```java
user.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
group.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
```

LDAPServerHostName

specifies the server host name of the
LDAP server, which may include a port number
(for example,

ldap.sun.com:389

),
and

LDAPName

specifies the entry name in the LDAP directory
(for example,

ou=People,o=Sun,c=US

and

ou=Groups,o=Sun,c=US

for user and group information, respectively).

The format in which the user's information must be stored in
the directory service is specified in RFC 2307. Specifically,
this

LoginModule

will search for the user's entry in the
directory service using the user's

uid

attribute,
where

uid=

username

. If the search succeeds,
this

LoginModule

will then
obtain the user's encrypted password from the retrieved entry
using the

userPassword

attribute.
This

LoginModule

assumes that the password is stored
as a byte array, which when converted to a

String

,
has the following format:

```java
"{crypt}
encrypted_password
"
```

The LDAP directory server must be configured
to permit read access to the userPassword attribute.
If the user entered a valid username and password,
this

LoginModule

associates a

UnixPrincipal

,

UnixNumericUserPrincipal

,
and the relevant UnixNumericGroupPrincipals with the

Subject

.

This LoginModule also recognizes the following

Configuration

options:

```java
debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this
LoginModule
clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.
```

**All Implemented Interfaces:** LoginModule

---

### Field Details

#### public final
String
USER_PROVIDER

JNDI Provider

**See Also:**
- Constant Field Values

---

#### public final
String
GROUP_PROVIDER

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public JndiLoginModule()

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
passwords, for example).
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

Prompt for username and password.
Verify the password against the relevant name service.

**Specified by:**
- login

in interface

LoginModule

**Returns:**
- true always, since this

LoginModule

should not be ignored.

**Throws:**
- FailedLoginException

- if the authentication fails.
- LoginException

- if this

LoginModule

is unable to perform the authentication.

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

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
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

This method removes the Principals
that were added by the

commit

method.

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

#### Class JndiLoginModule

java.lang.Object

- com.sun.security.auth.module.JndiLoginModule

com.sun.security.auth.module.JndiLoginModule

**All Implemented Interfaces:** LoginModule

```java
public class
JndiLoginModule

extends
Object

implements
LoginModule
```

The module prompts for a username and password
and then verifies the password against the password stored in
a directory service configured under JNDI.

This

LoginModule

interoperates with
any conformant JNDI service provider. To direct this

LoginModule

to use a specific JNDI service provider,
two options must be specified in the login

Configuration

for this

LoginModule

.

```java
user.provider.url=
name_service_url

group.provider.url=
name_service_url
```

name_service_url

specifies
the directory service and path where this

LoginModule

can access the relevant user and group information. Because this

LoginModule

only performs one-level searches to
find the relevant user information, the

URL

must point to a directory one level above where the user and group
information is stored in the directory service.
For example, to instruct this

LoginModule

to contact a NIS server, the following URLs must be specified:

```java
user.provider.url="nis://
NISServerHostName
/
NISDomain
/user"
group.provider.url="nis://
NISServerHostName
/
NISDomain
/system/group"
```

NISServerHostName

specifies the server host name of the
NIS server (for example,

nis.sun.com

, and

NISDomain

specifies the domain for that NIS server (for example,

jaas.sun.com

.
To contact an LDAP server, the following URLs must be specified:

```java
user.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
group.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
```

LDAPServerHostName

specifies the server host name of the
LDAP server, which may include a port number
(for example,

ldap.sun.com:389

),
and

LDAPName

specifies the entry name in the LDAP directory
(for example,

ou=People,o=Sun,c=US

and

ou=Groups,o=Sun,c=US

for user and group information, respectively).

The format in which the user's information must be stored in
the directory service is specified in RFC 2307. Specifically,
this

LoginModule

will search for the user's entry in the
directory service using the user's

uid

attribute,
where

uid=

username

. If the search succeeds,
this

LoginModule

will then
obtain the user's encrypted password from the retrieved entry
using the

userPassword

attribute.
This

LoginModule

assumes that the password is stored
as a byte array, which when converted to a

String

,
has the following format:

```java
"{crypt}
encrypted_password
"
```

The LDAP directory server must be configured
to permit read access to the userPassword attribute.
If the user entered a valid username and password,
this

LoginModule

associates a

UnixPrincipal

,

UnixNumericUserPrincipal

,
and the relevant UnixNumericGroupPrincipals with the

Subject

.

This LoginModule also recognizes the following

Configuration

options:

```java
debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this
LoginModule
clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.
```

public class

JndiLoginModule

extends

Object

implements

LoginModule

The module prompts for a username and password
and then verifies the password against the password stored in
a directory service configured under JNDI.

This

LoginModule

interoperates with
any conformant JNDI service provider. To direct this

LoginModule

to use a specific JNDI service provider,
two options must be specified in the login

Configuration

for this

LoginModule

.

```java
user.provider.url=
name_service_url

group.provider.url=
name_service_url
```

name_service_url

specifies
the directory service and path where this

LoginModule

can access the relevant user and group information. Because this

LoginModule

only performs one-level searches to
find the relevant user information, the

URL

must point to a directory one level above where the user and group
information is stored in the directory service.
For example, to instruct this

LoginModule

to contact a NIS server, the following URLs must be specified:

```java
user.provider.url="nis://
NISServerHostName
/
NISDomain
/user"
group.provider.url="nis://
NISServerHostName
/
NISDomain
/system/group"
```

NISServerHostName

specifies the server host name of the
NIS server (for example,

nis.sun.com

, and

NISDomain

specifies the domain for that NIS server (for example,

jaas.sun.com

.
To contact an LDAP server, the following URLs must be specified:

```java
user.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
group.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
```

LDAPServerHostName

specifies the server host name of the
LDAP server, which may include a port number
(for example,

ldap.sun.com:389

),
and

LDAPName

specifies the entry name in the LDAP directory
(for example,

ou=People,o=Sun,c=US

and

ou=Groups,o=Sun,c=US

for user and group information, respectively).

The format in which the user's information must be stored in
the directory service is specified in RFC 2307. Specifically,
this

LoginModule

will search for the user's entry in the
directory service using the user's

uid

attribute,
where

uid=

username

. If the search succeeds,
this

LoginModule

will then
obtain the user's encrypted password from the retrieved entry
using the

userPassword

attribute.
This

LoginModule

assumes that the password is stored
as a byte array, which when converted to a

String

,
has the following format:

```java
"{crypt}
encrypted_password
"
```

The LDAP directory server must be configured
to permit read access to the userPassword attribute.
If the user entered a valid username and password,
this

LoginModule

associates a

UnixPrincipal

,

UnixNumericUserPrincipal

,
and the relevant UnixNumericGroupPrincipals with the

Subject

.

This LoginModule also recognizes the following

Configuration

options:

```java
debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this
LoginModule
clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.
```

This

LoginModule

interoperates with
any conformant JNDI service provider. To direct this

LoginModule

to use a specific JNDI service provider,
two options must be specified in the login

Configuration

for this

LoginModule

.

```java
user.provider.url=
name_service_url

group.provider.url=
name_service_url
```

name_service_url

specifies
the directory service and path where this

LoginModule

can access the relevant user and group information. Because this

LoginModule

only performs one-level searches to
find the relevant user information, the

URL

must point to a directory one level above where the user and group
information is stored in the directory service.
For example, to instruct this

LoginModule

to contact a NIS server, the following URLs must be specified:

```java
user.provider.url="nis://
NISServerHostName
/
NISDomain
/user"
group.provider.url="nis://
NISServerHostName
/
NISDomain
/system/group"
```

NISServerHostName

specifies the server host name of the
NIS server (for example,

nis.sun.com

, and

NISDomain

specifies the domain for that NIS server (for example,

jaas.sun.com

.
To contact an LDAP server, the following URLs must be specified:

```java
user.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
group.provider.url="ldap://
LDAPServerHostName
/
LDAPName
"
```

LDAPServerHostName

specifies the server host name of the
LDAP server, which may include a port number
(for example,

ldap.sun.com:389

),
and

LDAPName

specifies the entry name in the LDAP directory
(for example,

ou=People,o=Sun,c=US

and

ou=Groups,o=Sun,c=US

for user and group information, respectively).

The format in which the user's information must be stored in
the directory service is specified in RFC 2307. Specifically,
this

LoginModule

will search for the user's entry in the
directory service using the user's

uid

attribute,
where

uid=

username

. If the search succeeds,
this

LoginModule

will then
obtain the user's encrypted password from the retrieved entry
using the

userPassword

attribute.
This

LoginModule

assumes that the password is stored
as a byte array, which when converted to a

String

,
has the following format:

```java
"{crypt}
encrypted_password
"
```

The LDAP directory server must be configured
to permit read access to the userPassword attribute.
If the user entered a valid username and password,
this

LoginModule

associates a

UnixPrincipal

,

UnixNumericUserPrincipal

,
and the relevant UnixNumericGroupPrincipals with the

Subject

.

This LoginModule also recognizes the following

Configuration

options:

```java
debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this
LoginModule
clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.
```

user.provider.url=

name_service_url

group.provider.url=

name_service_url

user.provider.url="nis://

NISServerHostName

/

NISDomain

/user"
group.provider.url="nis://

NISServerHostName

/

NISDomain

/system/group"

user.provider.url="ldap://

LDAPServerHostName

/

LDAPName

"
group.provider.url="ldap://

LDAPServerHostName

/

LDAPName

"

The format in which the user's information must be stored in
the directory service is specified in RFC 2307. Specifically,
this

LoginModule

will search for the user's entry in the
directory service using the user's

uid

attribute,
where

uid=

username

. If the search succeeds,
this

LoginModule

will then
obtain the user's encrypted password from the retrieved entry
using the

userPassword

attribute.
This

LoginModule

assumes that the password is stored
as a byte array, which when converted to a

String

,
has the following format:

```java
"{crypt}
encrypted_password
"
```

The LDAP directory server must be configured
to permit read access to the userPassword attribute.
If the user entered a valid username and password,
this

LoginModule

associates a

UnixPrincipal

,

UnixNumericUserPrincipal

,
and the relevant UnixNumericGroupPrincipals with the

Subject

.

This LoginModule also recognizes the following

Configuration

options:

```java
debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this
LoginModule
clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.
```

"{crypt}

encrypted_password

"

This LoginModule also recognizes the following

Configuration

options:

```java
debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this
LoginModule
clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.
```

debug if, true, debug messages are output to System.out.

useFirstPass if, true, this LoginModule retrieves the
username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, no attempt for a retry is made,
and the failure is reported back to the calling
application.

tryFirstPass if, true, this LoginModule retrieves the
the username and password from the module's shared state,
using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. The retrieved values are used for authentication.
If authentication fails, the module uses the
CallbackHandler to retrieve a new username and password,
and another attempt to authenticate is made.
If the authentication fails, the failure is reported
back to the calling application.

storePass if, true, this LoginModule stores the username and password
obtained from the CallbackHandler in the module's
shared state, using "javax.security.auth.login.name" and
"javax.security.auth.login.password" as the respective
keys. This is not performed if existing values already
exist for the username and password in the shared state,
or if authentication fails.

clearPass if, true, this

LoginModule

clears the
username and password stored in the module's shared state
after both phases of authentication (login and commit)
have completed.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

String

GROUP_PROVIDER

String

USER_PROVIDER

JNDI Provider

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JndiLoginModule

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

Prompt for username and password.

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

Field Summary

Fields

Modifier and Type

Field

Description

String

GROUP_PROVIDER

String

USER_PROVIDER

JNDI Provider

---

#### Field Summary

JNDI Provider

Constructor Summary

Constructors

Constructor

Description

JndiLoginModule

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

Prompt for username and password.

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

Prompt for username and password.

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

============ FIELD DETAIL ===========

- Field Detail

- USER_PROVIDER

```java
public final
String
USER_PROVIDER
```

JNDI Provider

**See Also:** Constant Field Values

- GROUP_PROVIDER

```java
public final
String
GROUP_PROVIDER
```

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JndiLoginModule

```java
public JndiLoginModule()
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
passwords, for example).
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

Prompt for username and password.
Verify the password against the relevant name service.

**Specified by:** login

in interface

LoginModule
**Returns:** true always, since this

LoginModule

should not be ignored.
**Throws:** FailedLoginException

- if the authentication fails.
**Throws:** LoginException

- if this

LoginModule

is unable to perform the authentication.

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

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
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

This method removes the Principals
that were added by the

commit

method.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases since this

LoginModule

should not be ignored.
**Throws:** LoginException

- if the logout fails.

Field Detail

- USER_PROVIDER

```java
public final
String
USER_PROVIDER
```

JNDI Provider

**See Also:** Constant Field Values

- GROUP_PROVIDER

```java
public final
String
GROUP_PROVIDER
```

**See Also:** Constant Field Values

---

#### Field Detail

USER_PROVIDER

```java
public final
String
USER_PROVIDER
```

JNDI Provider

**See Also:** Constant Field Values

---

#### USER_PROVIDER

public final

String

USER_PROVIDER

JNDI Provider

GROUP_PROVIDER

```java
public final
String
GROUP_PROVIDER
```

**See Also:** Constant Field Values

---

#### GROUP_PROVIDER

public final

String

GROUP_PROVIDER

Constructor Detail

- JndiLoginModule

```java
public JndiLoginModule()
```

---

#### Constructor Detail

JndiLoginModule

```java
public JndiLoginModule()
```

---

#### JndiLoginModule

public JndiLoginModule()

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
passwords, for example).
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

Prompt for username and password.
Verify the password against the relevant name service.

**Specified by:** login

in interface

LoginModule
**Returns:** true always, since this

LoginModule

should not be ignored.
**Throws:** FailedLoginException

- if the authentication fails.
**Throws:** LoginException

- if this

LoginModule

is unable to perform the authentication.

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

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
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

This method removes the Principals
that were added by the

commit

method.

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
passwords, for example).
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

Prompt for username and password.
Verify the password against the relevant name service.

**Specified by:** login

in interface

LoginModule
**Returns:** true always, since this

LoginModule

should not be ignored.
**Throws:** FailedLoginException

- if the authentication fails.
**Throws:** LoginException

- if this

LoginModule

is unable to perform the authentication.

---

#### login

public boolean login()
throws

LoginException

Prompt for username and password.
Verify the password against the relevant name service.

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

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
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

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
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

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates a

UnixPrincipal

with the

Subject

located in the

LoginModule

. If this LoginModule's own
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

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

and

commit

methods),
then this method cleans up any state that was originally saved.

logout

```java
public boolean logout()
throws
LoginException
```

Logout a user.

This method removes the Principals
that were added by the

commit

method.

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

This method removes the Principals
that were added by the

commit

method.

This method removes the Principals
that were added by the

commit

method.

---

