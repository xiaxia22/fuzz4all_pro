# Class NTLoginModule

**Source:** `jdk.security.auth\com\sun\security\auth\module\NTLoginModule.html`

### Class Description

```java
public class
NTLoginModule

extends
Object

implements
LoginModule
```

This

LoginModule

renders a user's NT security information as some number of

Principal

s
and associates them with a

Subject

.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

This LoginModule also recognizes the debugNative option.
If set to true in the login Configuration,
debug messages from the native component of the module
will be output to the output stream, System.out.

**All Implemented Interfaces:** LoginModule

---

### Field Details

*No entries found.*

### Constructor Details

#### public NTLoginModule()

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
passwords, for example). This particular LoginModule only
extracts the underlying NT system information, so this
parameter is ignored.
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

Import underlying NT system identity information.

**Specified by:**
- login

in interface

LoginModule

**Returns:**
- true in all cases since this

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

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates some
number of various

Principal

s
with the

Subject

located in the

LoginModuleContext

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

- if the commit fails.

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

Logout the user.

This method removes the

NTUserPrincipal

,

NTDomainPrincipal

,

NTSidUserPrincipal

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

s,
and

NTSidPrimaryGroupPrincipal

that may have been added by the

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

#### Class NTLoginModule

java.lang.Object

- com.sun.security.auth.module.NTLoginModule

com.sun.security.auth.module.NTLoginModule

**All Implemented Interfaces:** LoginModule

```java
public class
NTLoginModule

extends
Object

implements
LoginModule
```

This

LoginModule

renders a user's NT security information as some number of

Principal

s
and associates them with a

Subject

.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

This LoginModule also recognizes the debugNative option.
If set to true in the login Configuration,
debug messages from the native component of the module
will be output to the output stream, System.out.

**See Also:** LoginModule

public class

NTLoginModule

extends

Object

implements

LoginModule

This

LoginModule

renders a user's NT security information as some number of

Principal

s
and associates them with a

Subject

.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

This LoginModule also recognizes the debugNative option.
If set to true in the login Configuration,
debug messages from the native component of the module
will be output to the output stream, System.out.

This LoginModule recognizes the debug option.
If set to true in the login Configuration,
debug messages will be output to the output stream, System.out.

This LoginModule also recognizes the debugNative option.
If set to true in the login Configuration,
debug messages from the native component of the module
will be output to the output stream, System.out.

This LoginModule also recognizes the debugNative option.
If set to true in the login Configuration,
debug messages from the native component of the module
will be output to the output stream, System.out.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NTLoginModule

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

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

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

Import underlying NT system identity information.

boolean

logout

()

Logout the user.

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

NTLoginModule

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

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

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

Import underlying NT system identity information.

boolean

logout

()

Logout the user.

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

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

Initialize this

LoginModule

.

Import underlying NT system identity information.

Logout the user.

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

- NTLoginModule

```java
public NTLoginModule()
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
passwords, for example). This particular LoginModule only
extracts the underlying NT system information, so this
parameter is ignored.
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

Import underlying NT system identity information.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases since this

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

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates some
number of various

Principal

s
with the

Subject

located in the

LoginModuleContext

. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails.

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

Logout the user.

This method removes the

NTUserPrincipal

,

NTDomainPrincipal

,

NTSidUserPrincipal

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

s,
and

NTSidPrimaryGroupPrincipal

that may have been added by the

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

Constructor Detail

- NTLoginModule

```java
public NTLoginModule()
```

---

#### Constructor Detail

NTLoginModule

```java
public NTLoginModule()
```

---

#### NTLoginModule

public NTLoginModule()

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
passwords, for example). This particular LoginModule only
extracts the underlying NT system information, so this
parameter is ignored.
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

Import underlying NT system identity information.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases since this

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

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates some
number of various

Principal

s
with the

Subject

located in the

LoginModuleContext

. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails.

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

Logout the user.

This method removes the

NTUserPrincipal

,

NTDomainPrincipal

,

NTSidUserPrincipal

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

s,
and

NTSidPrimaryGroupPrincipal

that may have been added by the

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
passwords, for example). This particular LoginModule only
extracts the underlying NT system information, so this
parameter is ignored.
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

Import underlying NT system identity information.

**Specified by:** login

in interface

LoginModule
**Returns:** true in all cases since this

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

Import underlying NT system identity information.

commit

```java
public boolean commit()
throws
LoginException
```

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates some
number of various

Principal

s
with the

Subject

located in the

LoginModuleContext

. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

**Specified by:** commit

in interface

LoginModule
**Returns:** true if this LoginModule's own login and commit
attempts succeeded, or false otherwise.
**Throws:** LoginException

- if the commit fails.

---

#### commit

public boolean commit()
throws

LoginException

This method is called if the LoginContext's
overall authentication succeeded
(the relevant REQUIRED, REQUISITE, SUFFICIENT and OPTIONAL LoginModules
succeeded).

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates some
number of various

Principal

s
with the

Subject

located in the

LoginModuleContext

. If this LoginModule's own
authentication attempted failed, then this method removes
any state that was originally saved.

If this LoginModule's own authentication attempt
succeeded (checked by retrieving the private state saved by the

login

method), then this method associates some
number of various

Principal

s
with the

Subject

located in the

LoginModuleContext

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

Logout the user.

This method removes the

NTUserPrincipal

,

NTDomainPrincipal

,

NTSidUserPrincipal

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

s,
and

NTSidPrimaryGroupPrincipal

that may have been added by the

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

Logout the user.

This method removes the

NTUserPrincipal

,

NTDomainPrincipal

,

NTSidUserPrincipal

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

s,
and

NTSidPrimaryGroupPrincipal

that may have been added by the

commit

method.

This method removes the

NTUserPrincipal

,

NTDomainPrincipal

,

NTSidUserPrincipal

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

s,
and

NTSidPrimaryGroupPrincipal

that may have been added by the

commit

method.

---

