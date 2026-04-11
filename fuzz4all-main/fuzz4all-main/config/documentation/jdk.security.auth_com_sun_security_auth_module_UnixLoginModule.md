# Class UnixLoginModule

**Source:** `jdk.security.auth\com\sun\security\auth\module\UnixLoginModule.html`

### Class Description

```java
public class
UnixLoginModule

extends
Object

implements
LoginModule
```

This

LoginModule

imports a user's Unix

Principal

information (

UnixPrincipal

,

UnixNumericUserPrincipal

,
and

UnixNumericGroupPrincipal

)
and associates them with the current

Subject

.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

**All Implemented Interfaces:** LoginModule

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnixLoginModule()

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

Authenticate the user (first phase).

The implementation of this method attempts to retrieve the user's
Unix

Subject

information by making a native Unix
system call.

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

- if attempts to retrieve the underlying
system information fail.
- LoginException

- if the authentication fails

---

#### public boolean commit()
throws
LoginException

Commit the authentication (second phase).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:**
- commit

in interface

LoginModule

**Returns:**
- true if this LoginModule's own login and commit attempts
succeeded, or false otherwise.

**Throws:**
- LoginException

- if the commit fails

---

#### public boolean abort()
throws
LoginException

Abort the authentication (second phase).

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

**Specified by:**
- abort

in interface

LoginModule

**Returns:**
- false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.

**Throws:**
- LoginException

- if the abort fails

---

#### public boolean logout()
throws
LoginException

Logout the user

This method removes the Principals associated
with the

Subject

.

**Specified by:**
- logout

in interface

LoginModule

**Returns:**
- true in all cases (this

LoginModule

should not be ignored).

**Throws:**
- LoginException

- if the logout fails

---

### Additional Sections

#### Class UnixLoginModule

java.lang.Object

- com.sun.security.auth.module.UnixLoginModule

com.sun.security.auth.module.UnixLoginModule

**All Implemented Interfaces:** LoginModule

```java
public class
UnixLoginModule

extends
Object

implements
LoginModule
```

This

LoginModule

imports a user's Unix

Principal

information (

UnixPrincipal

,

UnixNumericUserPrincipal

,
and

UnixNumericGroupPrincipal

)
and associates them with the current

Subject

.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

public class

UnixLoginModule

extends

Object

implements

LoginModule

This

LoginModule

imports a user's Unix

Principal

information (

UnixPrincipal

,

UnixNumericUserPrincipal

,
and

UnixNumericGroupPrincipal

)
and associates them with the current

Subject

.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnixLoginModule

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

Abort the authentication (second phase).

boolean

commit

()

Commit the authentication (second phase).

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

Authenticate the user (first phase).

boolean

logout

()

Logout the user

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

UnixLoginModule

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

Abort the authentication (second phase).

boolean

commit

()

Commit the authentication (second phase).

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

Authenticate the user (first phase).

boolean

logout

()

Logout the user

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

Abort the authentication (second phase).

Commit the authentication (second phase).

Initialize this

LoginModule

.

Authenticate the user (first phase).

Logout the user

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

- UnixLoginModule

```java
public UnixLoginModule()
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

Authenticate the user (first phase).

The implementation of this method attempts to retrieve the user's
Unix

Subject

information by making a native Unix
system call.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** FailedLoginException

- if attempts to retrieve the underlying
system information fail.
**Throws:** LoginException

- if the authentication fails

- commit

```java
public boolean commit()
throws
LoginException
```

Commit the authentication (second phase).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit attempts
succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails

- abort

```java
public boolean abort()
throws
LoginException
```

Abort the authentication (second phase).

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

**Specified by:** abort

in interface

LoginModule
**Returns:** false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.
**Throws:** LoginException

- if the abort fails

- logout

```java
public boolean logout()
throws
LoginException
```

Logout the user

This method removes the Principals associated
with the

Subject

.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** LoginException

- if the logout fails

Constructor Detail

- UnixLoginModule

```java
public UnixLoginModule()
```

---

#### Constructor Detail

UnixLoginModule

```java
public UnixLoginModule()
```

---

#### UnixLoginModule

public UnixLoginModule()

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

Authenticate the user (first phase).

The implementation of this method attempts to retrieve the user's
Unix

Subject

information by making a native Unix
system call.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** FailedLoginException

- if attempts to retrieve the underlying
system information fail.
**Throws:** LoginException

- if the authentication fails

- commit

```java
public boolean commit()
throws
LoginException
```

Commit the authentication (second phase).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit attempts
succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails

- abort

```java
public boolean abort()
throws
LoginException
```

Abort the authentication (second phase).

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

**Specified by:** abort

in interface

LoginModule
**Returns:** false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.
**Throws:** LoginException

- if the abort fails

- logout

```java
public boolean logout()
throws
LoginException
```

Logout the user

This method removes the Principals associated
with the

Subject

.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** LoginException

- if the logout fails

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

Authenticate the user (first phase).

The implementation of this method attempts to retrieve the user's
Unix

Subject

information by making a native Unix
system call.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** FailedLoginException

- if attempts to retrieve the underlying
system information fail.
**Throws:** LoginException

- if the authentication fails

---

#### login

public boolean login()
throws

LoginException

Authenticate the user (first phase).

The implementation of this method attempts to retrieve the user's
Unix

Subject

information by making a native Unix
system call.

The implementation of this method attempts to retrieve the user's
Unix

Subject

information by making a native Unix
system call.

commit

```java
public boolean commit()
throws
LoginException
```

Commit the authentication (second phase).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit attempts
succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails

---

#### commit

public boolean commit()
throws

LoginException

Commit the authentication (second phase).

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

If this LoginModule's own authentication attempt
succeeded (the importing of the Unix authentication information
succeeded), then this method associates the Unix Principals
with the

Subject

currently tied to the

LoginModule

. If this LoginModule's
authentication attempted failed, then this method removes
any state that was originally saved.

abort

```java
public boolean abort()
throws
LoginException
```

Abort the authentication (second phase).

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

**Specified by:** abort

in interface

LoginModule
**Returns:** false if this LoginModule's own login and/or commit attempts
failed, and true otherwise.
**Throws:** LoginException

- if the abort fails

---

#### abort

public boolean abort()
throws

LoginException

Abort the authentication (second phase).

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

This method is called if the LoginContext's
overall authentication failed.
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
did not succeed).

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

This method cleans up any state that was originally saved
as part of the authentication attempt from the

login

and

commit

methods.

logout

```java
public boolean logout()
throws
LoginException
```

Logout the user

This method removes the Principals associated
with the

Subject

.

**Specified by:** logout

in interface

LoginModule
**Returns:** true in all cases (this

LoginModule

should not be ignored).
**Throws:** LoginException

- if the logout fails

---

#### logout

public boolean logout()
throws

LoginException

Logout the user

This method removes the Principals associated
with the

Subject

.

This method removes the Principals associated
with the

Subject

.

---

