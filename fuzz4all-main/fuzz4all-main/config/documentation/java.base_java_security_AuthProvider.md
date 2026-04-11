# Class AuthProvider

**Source:** `java.base\java\security\AuthProvider.html`

### Class Description

```java
public abstract class
AuthProvider

extends
Provider
```

This class defines login and logout methods for a provider.

While callers may invoke

login

directly,
the provider may also invoke

login

on behalf of callers
if it determines that a login must be performed
prior to certain operations.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

Object

,​

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

#### @Deprecated
(
since
="9")
protected AuthProvider​(
String
name,
double version,

String
info)

Constructs a provider with the specified name, version number,
and information.

**Parameters:**
- name

- the provider name.
- version

- the provider version number.
- info

- a description of the provider and its services.

---

#### protected AuthProvider​(
String
name,

String
versionStr,

String
info)

Constructs a provider with the specified name, version string,
and information.

**Parameters:**
- name

- the provider name.
- versionStr

- the provider version string.
- info

- a description of the provider and its services.

**Since:**
- 9

---

### Method Details

#### public abstract void login​(
Subject
subject,

CallbackHandler
handler)
throws
LoginException

Log in to this provider.

The provider relies on a

CallbackHandler

to obtain authentication information from the caller
(a PIN, for example). If the caller passes a

null

handler to this method, the provider uses the handler set in the

setCallbackHandler

method.
If no handler was set in that method, the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:**
- subject

- the

Subject

which may contain
principals/credentials used for authentication,
or may be populated with additional principals/credentials
after successful authentication has completed.
This parameter may be

null

.
- handler

- the

CallbackHandler

used by
this provider to obtain authentication information
from the caller, which may be

null

**Throws:**
- IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
- LoginException

- if the login operation fails
- SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

#### public abstract void logout()
throws
LoginException

Log out from this provider.

**Throws:**
- IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
- LoginException

- if the logout operation fails
- SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

#### public abstract void setCallbackHandler​(
CallbackHandler
handler)

Set a

CallbackHandler

.

The provider uses this handler if one is not passed to the

login

method. The provider also uses this handler
if it invokes

login

on behalf of callers.
In either case if a handler is not set via this method,
the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:**
- handler

- a

CallbackHandler

for obtaining
authentication information, which may be

null

**Throws:**
- IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
- SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

### Additional Sections

#### Class AuthProvider

java.lang.Object

- java.util.Dictionary

<K,​V>
- - java.util.Hashtable

<

Object

,​

Object

>
- - java.util.Properties
- - java.security.Provider
- - java.security.AuthProvider

java.util.Dictionary

<K,​V>

- java.util.Hashtable

<

Object

,​

Object

>
- - java.util.Properties
- - java.security.Provider
- - java.security.AuthProvider

java.util.Hashtable

<

Object

,​

Object

>

- java.util.Properties
- - java.security.Provider
- - java.security.AuthProvider

java.util.Properties

- java.security.Provider
- - java.security.AuthProvider

java.security.Provider

- java.security.AuthProvider

java.security.AuthProvider

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

Object

,​

Object

>

```java
public abstract class
AuthProvider

extends
Provider
```

This class defines login and logout methods for a provider.

While callers may invoke

login

directly,
the provider may also invoke

login

on behalf of callers
if it determines that a login must be performed
prior to certain operations.

**Since:** 1.5
**See Also:** Serialized Form

public abstract class

AuthProvider

extends

Provider

This class defines login and logout methods for a provider.

While callers may invoke

login

directly,
the provider may also invoke

login

on behalf of callers
if it determines that a login must be performed
prior to certain operations.

While callers may invoke

login

directly,
the provider may also invoke

login

on behalf of callers
if it determines that a login must be performed
prior to certain operations.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.security.

Provider

Provider.Service

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

Properties

defaults

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AuthProvider

​(

String

name,
double version,

String

info)

Deprecated.

use

AuthProvider(String, String, String)

instead.

protected

AuthProvider

​(

String

name,

String

versionStr,

String

info)

Constructs a provider with the specified name, version string,
and information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

login

​(

Subject

subject,

CallbackHandler

handler)

Log in to this provider.

abstract void

logout

()

Log out from this provider.

abstract void

setCallbackHandler

​(

CallbackHandler

handler)

Set a

CallbackHandler

.

- Methods declared in class java.security.

Provider

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

configure

,

entrySet

,

forEach

,

getInfo

,

getName

,

getOrDefault

,

getService

,

getServices

,

getVersion

,

getVersionStr

,

isConfigured

,

keySet

,

load

,

merge

,

put

,

putAll

,

putIfAbsent

,

putService

,

remove

,

remove

,

removeService

,

replace

,

replace

,

replaceAll

,

toString

,

values

- Methods declared in class java.util.

Properties

getProperty

,

getProperty

,

list

,

list

,

load

,

loadFromXML

,

propertyNames

,

save

,

setProperty

,

store

,

store

,

storeToXML

,

storeToXML

,

storeToXML

,

stringPropertyNames

- Methods declared in class java.util.

Hashtable

clone

,

contains

,

containsKey

,

containsValue

,

elements

,

equals

,

get

,

hashCode

,

isEmpty

,

keys

,

rehash

,

size

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class java.security.

Provider

Provider.Service

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.security.

Provider

Provider.Service

---

#### Nested classes/interfaces declared in class java.security. Provider

Field Summary

- Fields declared in class java.util.

Properties

defaults

---

#### Field Summary

Fields declared in class java.util.

Properties

defaults

---

#### Fields declared in class java.util. Properties

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AuthProvider

​(

String

name,
double version,

String

info)

Deprecated.

use

AuthProvider(String, String, String)

instead.

protected

AuthProvider

​(

String

name,

String

versionStr,

String

info)

Constructs a provider with the specified name, version string,
and information.

---

#### Constructor Summary

Deprecated.

use

AuthProvider(String, String, String)

instead.

Constructs a provider with the specified name, version string,
and information.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

login

​(

Subject

subject,

CallbackHandler

handler)

Log in to this provider.

abstract void

logout

()

Log out from this provider.

abstract void

setCallbackHandler

​(

CallbackHandler

handler)

Set a

CallbackHandler

.

- Methods declared in class java.security.

Provider

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

configure

,

entrySet

,

forEach

,

getInfo

,

getName

,

getOrDefault

,

getService

,

getServices

,

getVersion

,

getVersionStr

,

isConfigured

,

keySet

,

load

,

merge

,

put

,

putAll

,

putIfAbsent

,

putService

,

remove

,

remove

,

removeService

,

replace

,

replace

,

replaceAll

,

toString

,

values

- Methods declared in class java.util.

Properties

getProperty

,

getProperty

,

list

,

list

,

load

,

loadFromXML

,

propertyNames

,

save

,

setProperty

,

store

,

store

,

storeToXML

,

storeToXML

,

storeToXML

,

stringPropertyNames

- Methods declared in class java.util.

Hashtable

clone

,

contains

,

containsKey

,

containsValue

,

elements

,

equals

,

get

,

hashCode

,

isEmpty

,

keys

,

rehash

,

size

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Log in to this provider.

Log out from this provider.

Set a

CallbackHandler

.

Methods declared in class java.security.

Provider

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

configure

,

entrySet

,

forEach

,

getInfo

,

getName

,

getOrDefault

,

getService

,

getServices

,

getVersion

,

getVersionStr

,

isConfigured

,

keySet

,

load

,

merge

,

put

,

putAll

,

putIfAbsent

,

putService

,

remove

,

remove

,

removeService

,

replace

,

replace

,

replaceAll

,

toString

,

values

---

#### Methods declared in class java.security. Provider

Methods declared in class java.util.

Properties

getProperty

,

getProperty

,

list

,

list

,

load

,

loadFromXML

,

propertyNames

,

save

,

setProperty

,

store

,

store

,

storeToXML

,

storeToXML

,

storeToXML

,

stringPropertyNames

---

#### Methods declared in class java.util. Properties

Methods declared in class java.util.

Hashtable

clone

,

contains

,

containsKey

,

containsValue

,

elements

,

equals

,

get

,

hashCode

,

isEmpty

,

keys

,

rehash

,

size

---

#### Methods declared in class java.util. Hashtable

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

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

- AuthProvider

```java
@Deprecated
(
since
="9")
protected AuthProvider​(
String
name,
double version,

String
info)
```

Deprecated.

use

AuthProvider(String, String, String)

instead.

Constructs a provider with the specified name, version number,
and information.

**Parameters:** name

- the provider name.
**Parameters:** version

- the provider version number.
**Parameters:** info

- a description of the provider and its services.

- AuthProvider

```java
protected AuthProvider​(
String
name,

String
versionStr,

String
info)
```

Constructs a provider with the specified name, version string,
and information.

**Parameters:** name

- the provider name.
**Parameters:** versionStr

- the provider version string.
**Parameters:** info

- a description of the provider and its services.
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- login

```java
public abstract void login​(
Subject
subject,

CallbackHandler
handler)
throws
LoginException
```

Log in to this provider.

The provider relies on a

CallbackHandler

to obtain authentication information from the caller
(a PIN, for example). If the caller passes a

null

handler to this method, the provider uses the handler set in the

setCallbackHandler

method.
If no handler was set in that method, the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:** subject

- the

Subject

which may contain
principals/credentials used for authentication,
or may be populated with additional principals/credentials
after successful authentication has completed.
This parameter may be

null

.
**Parameters:** handler

- the

CallbackHandler

used by
this provider to obtain authentication information
from the caller, which may be

null
**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** LoginException

- if the login operation fails
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

- logout

```java
public abstract void logout()
throws
LoginException
```

Log out from this provider.

**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** LoginException

- if the logout operation fails
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

- setCallbackHandler

```java
public abstract void setCallbackHandler​(
CallbackHandler
handler)
```

Set a

CallbackHandler

.

The provider uses this handler if one is not passed to the

login

method. The provider also uses this handler
if it invokes

login

on behalf of callers.
In either case if a handler is not set via this method,
the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:** handler

- a

CallbackHandler

for obtaining
authentication information, which may be

null
**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

Constructor Detail

- AuthProvider

```java
@Deprecated
(
since
="9")
protected AuthProvider​(
String
name,
double version,

String
info)
```

Deprecated.

use

AuthProvider(String, String, String)

instead.

Constructs a provider with the specified name, version number,
and information.

**Parameters:** name

- the provider name.
**Parameters:** version

- the provider version number.
**Parameters:** info

- a description of the provider and its services.

- AuthProvider

```java
protected AuthProvider​(
String
name,

String
versionStr,

String
info)
```

Constructs a provider with the specified name, version string,
and information.

**Parameters:** name

- the provider name.
**Parameters:** versionStr

- the provider version string.
**Parameters:** info

- a description of the provider and its services.
**Since:** 9

---

#### Constructor Detail

AuthProvider

```java
@Deprecated
(
since
="9")
protected AuthProvider​(
String
name,
double version,

String
info)
```

Deprecated.

use

AuthProvider(String, String, String)

instead.

Constructs a provider with the specified name, version number,
and information.

**Parameters:** name

- the provider name.
**Parameters:** version

- the provider version number.
**Parameters:** info

- a description of the provider and its services.

---

#### AuthProvider

@Deprecated

(

since

="9")
protected AuthProvider​(

String

name,
double version,

String

info)

Constructs a provider with the specified name, version number,
and information.

AuthProvider

```java
protected AuthProvider​(
String
name,

String
versionStr,

String
info)
```

Constructs a provider with the specified name, version string,
and information.

**Parameters:** name

- the provider name.
**Parameters:** versionStr

- the provider version string.
**Parameters:** info

- a description of the provider and its services.
**Since:** 9

---

#### AuthProvider

protected AuthProvider​(

String

name,

String

versionStr,

String

info)

Constructs a provider with the specified name, version string,
and information.

Method Detail

- login

```java
public abstract void login​(
Subject
subject,

CallbackHandler
handler)
throws
LoginException
```

Log in to this provider.

The provider relies on a

CallbackHandler

to obtain authentication information from the caller
(a PIN, for example). If the caller passes a

null

handler to this method, the provider uses the handler set in the

setCallbackHandler

method.
If no handler was set in that method, the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:** subject

- the

Subject

which may contain
principals/credentials used for authentication,
or may be populated with additional principals/credentials
after successful authentication has completed.
This parameter may be

null

.
**Parameters:** handler

- the

CallbackHandler

used by
this provider to obtain authentication information
from the caller, which may be

null
**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** LoginException

- if the login operation fails
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

- logout

```java
public abstract void logout()
throws
LoginException
```

Log out from this provider.

**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** LoginException

- if the logout operation fails
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

- setCallbackHandler

```java
public abstract void setCallbackHandler​(
CallbackHandler
handler)
```

Set a

CallbackHandler

.

The provider uses this handler if one is not passed to the

login

method. The provider also uses this handler
if it invokes

login

on behalf of callers.
In either case if a handler is not set via this method,
the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:** handler

- a

CallbackHandler

for obtaining
authentication information, which may be

null
**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

#### Method Detail

login

```java
public abstract void login​(
Subject
subject,

CallbackHandler
handler)
throws
LoginException
```

Log in to this provider.

The provider relies on a

CallbackHandler

to obtain authentication information from the caller
(a PIN, for example). If the caller passes a

null

handler to this method, the provider uses the handler set in the

setCallbackHandler

method.
If no handler was set in that method, the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:** subject

- the

Subject

which may contain
principals/credentials used for authentication,
or may be populated with additional principals/credentials
after successful authentication has completed.
This parameter may be

null

.
**Parameters:** handler

- the

CallbackHandler

used by
this provider to obtain authentication information
from the caller, which may be

null
**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** LoginException

- if the login operation fails
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

#### login

public abstract void login​(

Subject

subject,

CallbackHandler

handler)
throws

LoginException

Log in to this provider.

The provider relies on a

CallbackHandler

to obtain authentication information from the caller
(a PIN, for example). If the caller passes a

null

handler to this method, the provider uses the handler set in the

setCallbackHandler

method.
If no handler was set in that method, the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

The provider relies on a

CallbackHandler

to obtain authentication information from the caller
(a PIN, for example). If the caller passes a

null

handler to this method, the provider uses the handler set in the

setCallbackHandler

method.
If no handler was set in that method, the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

logout

```java
public abstract void logout()
throws
LoginException
```

Log out from this provider.

**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** LoginException

- if the logout operation fails
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

#### logout

public abstract void logout()
throws

LoginException

Log out from this provider.

setCallbackHandler

```java
public abstract void setCallbackHandler​(
CallbackHandler
handler)
```

Set a

CallbackHandler

.

The provider uses this handler if one is not passed to the

login

method. The provider also uses this handler
if it invokes

login

on behalf of callers.
In either case if a handler is not set via this method,
the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

**Parameters:** handler

- a

CallbackHandler

for obtaining
authentication information, which may be

null
**Throws:** IllegalStateException

- if the provider requires configuration
and

Provider.configure(java.lang.String)

has not been called
**Throws:** SecurityException

- if the caller does not pass a
security check for

SecurityPermission("authProvider.name")

,
where

name

is the value returned by
this provider's

getName

method

---

#### setCallbackHandler

public abstract void setCallbackHandler​(

CallbackHandler

handler)

Set a

CallbackHandler

.

The provider uses this handler if one is not passed to the

login

method. The provider also uses this handler
if it invokes

login

on behalf of callers.
In either case if a handler is not set via this method,
the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

The provider uses this handler if one is not passed to the

login

method. The provider also uses this handler
if it invokes

login

on behalf of callers.
In either case if a handler is not set via this method,
the provider queries the

auth.login.defaultCallbackHandler

security property
for the fully qualified class name of a default handler implementation.
If the security property is not set,
the provider is assumed to have alternative means
for obtaining authentication information.

---

