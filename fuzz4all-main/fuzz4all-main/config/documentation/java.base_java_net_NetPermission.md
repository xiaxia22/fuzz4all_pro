# Class NetPermission

**Source:** `java.base\java\net\NetPermission.html`

### Class Description

```java
public final class
NetPermission

extends
BasicPermission
```

This class is for various network permissions.
A NetPermission contains a name (also referred to as a "target name") but
no actions list; you either have the named permission
or you don't.

The target name is the name of the network permission (see below). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "foo.*" and "*" signify a wildcard
match, while "*foo" and "a*b" do not.

The following table lists all the possible NetPermission target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

allowHttpTrace

The ability to use the HTTP TRACE method in HttpURLConnection.

Malicious code using HTTP TRACE could get access to security sensitive
information in the HTTP headers (such as cookies) that it might not
otherwise have access to.

getCookieHandler

The ability to get the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can get a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

getNetworkInformation

The ability to retrieve all information about local network interfaces.

Malicious code can read information about network hardware such as
MAC addresses, which could be used to construct local IPv6 addresses.

getProxySelector

The ability to get the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can get a ProxySelector to discover proxy
hosts and ports on internal networks, which could then become
targets for attack.

getResponseCache

The ability to get the response cache that provides
access to a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information.

requestPasswordAuthentication

The ability
to ask the authenticator registered with the system for
a password

Malicious code may steal this password.

setCookieHandler

The ability to set the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can set a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

setDefaultAuthenticator

The ability to set the
way authentication information is retrieved when
a proxy or HTTP server asks for authentication

Malicious
code can set an authenticator that monitors and steals user
authentication input as it retrieves the input from the user.

setProxySelector

The ability to set the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can set a ProxySelector that directs network
traffic to an arbitrary network host.

setResponseCache

The ability to set the response cache that provides access to
a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information, or create false
entries in the response cache.

specifyStreamHandler

The ability
to specify a stream handler when constructing a URL

Malicious code may create a URL with resources that it would
normally not have access to (like file:/foo/fum/), specifying a
stream handler that gets the actual bytes from someplace it does
have access to. Thus it might be able to trick the system into
creating a ProtectionDomain/CodeSource for a class even though
that class really didn't come from that location.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public NetPermission​(
String
name)

Creates a new NetPermission with the specified name.
The name is the symbolic name of the NetPermission, such as
"setDefaultAuthenticator", etc. An asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match.

**Parameters:**
- name

- the name of the NetPermission.

**Throws:**
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty.

---

#### public NetPermission​(
String
name,

String
actions)

Creates a new NetPermission object with the specified name.
The name is the symbolic name of the NetPermission, and the
actions String is currently unused and should be null.

**Parameters:**
- name

- the name of the NetPermission.
- actions

- should be null.

**Throws:**
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NetPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.net.NetPermission

java.security.Permission

- java.security.BasicPermission
- - java.net.NetPermission

java.security.BasicPermission

- java.net.NetPermission

java.net.NetPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
NetPermission

extends
BasicPermission
```

This class is for various network permissions.
A NetPermission contains a name (also referred to as a "target name") but
no actions list; you either have the named permission
or you don't.

The target name is the name of the network permission (see below). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "foo.*" and "*" signify a wildcard
match, while "*foo" and "a*b" do not.

The following table lists all the possible NetPermission target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

allowHttpTrace

The ability to use the HTTP TRACE method in HttpURLConnection.

Malicious code using HTTP TRACE could get access to security sensitive
information in the HTTP headers (such as cookies) that it might not
otherwise have access to.

getCookieHandler

The ability to get the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can get a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

getNetworkInformation

The ability to retrieve all information about local network interfaces.

Malicious code can read information about network hardware such as
MAC addresses, which could be used to construct local IPv6 addresses.

getProxySelector

The ability to get the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can get a ProxySelector to discover proxy
hosts and ports on internal networks, which could then become
targets for attack.

getResponseCache

The ability to get the response cache that provides
access to a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information.

requestPasswordAuthentication

The ability
to ask the authenticator registered with the system for
a password

Malicious code may steal this password.

setCookieHandler

The ability to set the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can set a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

setDefaultAuthenticator

The ability to set the
way authentication information is retrieved when
a proxy or HTTP server asks for authentication

Malicious
code can set an authenticator that monitors and steals user
authentication input as it retrieves the input from the user.

setProxySelector

The ability to set the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can set a ProxySelector that directs network
traffic to an arbitrary network host.

setResponseCache

The ability to set the response cache that provides access to
a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information, or create false
entries in the response cache.

specifyStreamHandler

The ability
to specify a stream handler when constructing a URL

Malicious code may create a URL with resources that it would
normally not have access to (like file:/foo/fum/), specifying a
stream handler that gets the actual bytes from someplace it does
have access to. Thus it might be able to trick the system into
creating a ProtectionDomain/CodeSource for a class even though
that class really didn't come from that location.

**Since:** 1.2
**See Also:** BasicPermission

,

Permission

,

Permissions

,

PermissionCollection

,

SecurityManager

,

Serialized Form

public final class

NetPermission

extends

BasicPermission

This class is for various network permissions.
A NetPermission contains a name (also referred to as a "target name") but
no actions list; you either have the named permission
or you don't.

The target name is the name of the network permission (see below). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "foo.*" and "*" signify a wildcard
match, while "*foo" and "a*b" do not.

The following table lists all the possible NetPermission target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

allowHttpTrace

The ability to use the HTTP TRACE method in HttpURLConnection.

Malicious code using HTTP TRACE could get access to security sensitive
information in the HTTP headers (such as cookies) that it might not
otherwise have access to.

getCookieHandler

The ability to get the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can get a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

getNetworkInformation

The ability to retrieve all information about local network interfaces.

Malicious code can read information about network hardware such as
MAC addresses, which could be used to construct local IPv6 addresses.

getProxySelector

The ability to get the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can get a ProxySelector to discover proxy
hosts and ports on internal networks, which could then become
targets for attack.

getResponseCache

The ability to get the response cache that provides
access to a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information.

requestPasswordAuthentication

The ability
to ask the authenticator registered with the system for
a password

Malicious code may steal this password.

setCookieHandler

The ability to set the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can set a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

setDefaultAuthenticator

The ability to set the
way authentication information is retrieved when
a proxy or HTTP server asks for authentication

Malicious
code can set an authenticator that monitors and steals user
authentication input as it retrieves the input from the user.

setProxySelector

The ability to set the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can set a ProxySelector that directs network
traffic to an arbitrary network host.

setResponseCache

The ability to set the response cache that provides access to
a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information, or create false
entries in the response cache.

specifyStreamHandler

The ability
to specify a stream handler when constructing a URL

Malicious code may create a URL with resources that it would
normally not have access to (like file:/foo/fum/), specifying a
stream handler that gets the actual bytes from someplace it does
have access to. Thus it might be able to trick the system into
creating a ProtectionDomain/CodeSource for a class even though
that class really didn't come from that location.

The target name is the name of the network permission (see below). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "foo.*" and "*" signify a wildcard
match, while "*foo" and "a*b" do not.

The following table lists all the possible NetPermission target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

allowHttpTrace

The ability to use the HTTP TRACE method in HttpURLConnection.

Malicious code using HTTP TRACE could get access to security sensitive
information in the HTTP headers (such as cookies) that it might not
otherwise have access to.

getCookieHandler

The ability to get the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can get a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

getNetworkInformation

The ability to retrieve all information about local network interfaces.

Malicious code can read information about network hardware such as
MAC addresses, which could be used to construct local IPv6 addresses.

getProxySelector

The ability to get the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can get a ProxySelector to discover proxy
hosts and ports on internal networks, which could then become
targets for attack.

getResponseCache

The ability to get the response cache that provides
access to a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information.

requestPasswordAuthentication

The ability
to ask the authenticator registered with the system for
a password

Malicious code may steal this password.

setCookieHandler

The ability to set the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can set a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

setDefaultAuthenticator

The ability to set the
way authentication information is retrieved when
a proxy or HTTP server asks for authentication

Malicious
code can set an authenticator that monitors and steals user
authentication input as it retrieves the input from the user.

setProxySelector

The ability to set the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can set a ProxySelector that directs network
traffic to an arbitrary network host.

setResponseCache

The ability to set the response cache that provides access to
a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information, or create false
entries in the response cache.

specifyStreamHandler

The ability
to specify a stream handler when constructing a URL

Malicious code may create a URL with resources that it would
normally not have access to (like file:/foo/fum/), specifying a
stream handler that gets the actual bytes from someplace it does
have access to. Thus it might be able to trick the system into
creating a ProtectionDomain/CodeSource for a class even though
that class really didn't come from that location.

The following table lists all the possible NetPermission target names,
and for each provides a description of what the permission allows
and a discussion of the risks of granting code the permission.

Permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

allowHttpTrace

The ability to use the HTTP TRACE method in HttpURLConnection.

Malicious code using HTTP TRACE could get access to security sensitive
information in the HTTP headers (such as cookies) that it might not
otherwise have access to.

getCookieHandler

The ability to get the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can get a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

getNetworkInformation

The ability to retrieve all information about local network interfaces.

Malicious code can read information about network hardware such as
MAC addresses, which could be used to construct local IPv6 addresses.

getProxySelector

The ability to get the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can get a ProxySelector to discover proxy
hosts and ports on internal networks, which could then become
targets for attack.

getResponseCache

The ability to get the response cache that provides
access to a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information.

requestPasswordAuthentication

The ability
to ask the authenticator registered with the system for
a password

Malicious code may steal this password.

setCookieHandler

The ability to set the cookie handler that processes highly
security sensitive cookie information for an Http session.

Malicious code can set a cookie handler to obtain access to
highly security sensitive cookie information. Some web servers
use cookies to save user private information such as access
control information, or to track user browsing habit.

setDefaultAuthenticator

The ability to set the
way authentication information is retrieved when
a proxy or HTTP server asks for authentication

Malicious
code can set an authenticator that monitors and steals user
authentication input as it retrieves the input from the user.

setProxySelector

The ability to set the proxy selector used to make decisions
on which proxies to use when making network connections.

Malicious code can set a ProxySelector that directs network
traffic to an arbitrary network host.

setResponseCache

The ability to set the response cache that provides access to
a local response cache.

Malicious code getting access to the local response cache
could access security sensitive information, or create false
entries in the response cache.

specifyStreamHandler

The ability
to specify a stream handler when constructing a URL

Malicious code may create a URL with resources that it would
normally not have access to (like file:/foo/fum/), specifying a
stream handler that gets the actual bytes from someplace it does
have access to. Thus it might be able to trick the system into
creating a ProtectionDomain/CodeSource for a class even though
that class really didn't come from that location.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NetPermission

​(

String

name)

Creates a new NetPermission with the specified name.

NetPermission

​(

String

name,

String

actions)

Creates a new NetPermission object with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

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

Constructor Summary

Constructors

Constructor

Description

NetPermission

​(

String

name)

Creates a new NetPermission with the specified name.

NetPermission

​(

String

name,

String

actions)

Creates a new NetPermission object with the specified name.

---

#### Constructor Summary

Creates a new NetPermission with the specified name.

Creates a new NetPermission object with the specified name.

Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

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

Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

---

#### Methods declared in class java.security. BasicPermission

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

Methods declared in class java.lang.

Object

clone

,

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

- NetPermission

```java
public NetPermission​(
String
name)
```

Creates a new NetPermission with the specified name.
The name is the symbolic name of the NetPermission, such as
"setDefaultAuthenticator", etc. An asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match.

**Parameters:** name

- the name of the NetPermission.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

- NetPermission

```java
public NetPermission​(
String
name,

String
actions)
```

Creates a new NetPermission object with the specified name.
The name is the symbolic name of the NetPermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the NetPermission.
**Parameters:** actions

- should be null.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

Constructor Detail

- NetPermission

```java
public NetPermission​(
String
name)
```

Creates a new NetPermission with the specified name.
The name is the symbolic name of the NetPermission, such as
"setDefaultAuthenticator", etc. An asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match.

**Parameters:** name

- the name of the NetPermission.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

- NetPermission

```java
public NetPermission​(
String
name,

String
actions)
```

Creates a new NetPermission object with the specified name.
The name is the symbolic name of the NetPermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the NetPermission.
**Parameters:** actions

- should be null.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### Constructor Detail

NetPermission

```java
public NetPermission​(
String
name)
```

Creates a new NetPermission with the specified name.
The name is the symbolic name of the NetPermission, such as
"setDefaultAuthenticator", etc. An asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match.

**Parameters:** name

- the name of the NetPermission.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### NetPermission

public NetPermission​(

String

name)

Creates a new NetPermission with the specified name.
The name is the symbolic name of the NetPermission, such as
"setDefaultAuthenticator", etc. An asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match.

NetPermission

```java
public NetPermission​(
String
name,

String
actions)
```

Creates a new NetPermission object with the specified name.
The name is the symbolic name of the NetPermission, and the
actions String is currently unused and should be null.

**Parameters:** name

- the name of the NetPermission.
**Parameters:** actions

- should be null.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### NetPermission

public NetPermission​(

String

name,

String

actions)

Creates a new NetPermission object with the specified name.
The name is the symbolic name of the NetPermission, and the
actions String is currently unused and should be null.

---

