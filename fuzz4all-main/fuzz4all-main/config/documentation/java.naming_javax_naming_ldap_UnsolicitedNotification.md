# Interface UnsolicitedNotification

**Source:** `java.naming\javax\naming\ldap\UnsolicitedNotification.html`

### Class Description

```java
public interface
UnsolicitedNotification

extends
ExtendedResponse
,
HasControls
```

This interface represents an unsolicited notification as defined in

RFC 2251

.
An unsolicited notification is sent by the LDAP server to the LDAP
client without any provocation from the client.
Its format is that of an extended response (

ExtendedResponse

).

**All Superinterfaces:** ExtendedResponse

,

HasControls

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
[] getReferrals()

Retrieves the referral(s) sent by the server.

**Returns:**
- A possibly null array of referrals, each of which is represented
by a URL string. If null, no referral was sent by the server.

---

#### NamingException
getException()

Retrieves the exception as constructed using information
sent by the server.

**Returns:**
- A possibly null exception as constructed using information
sent by the server. If null, a "success" status was indicated by
the server.

---

### Additional Sections

#### Interface UnsolicitedNotification

**All Superinterfaces:** ExtendedResponse

,

HasControls

,

Serializable

```java
public interface
UnsolicitedNotification

extends
ExtendedResponse
,
HasControls
```

This interface represents an unsolicited notification as defined in

RFC 2251

.
An unsolicited notification is sent by the LDAP server to the LDAP
client without any provocation from the client.
Its format is that of an extended response (

ExtendedResponse

).

**Since:** 1.3
**See Also:** ExtendedResponse

,

UnsolicitedNotificationEvent

,

UnsolicitedNotificationListener

public interface

UnsolicitedNotification

extends

ExtendedResponse

,

HasControls

This interface represents an unsolicited notification as defined in

RFC 2251

.
An unsolicited notification is sent by the LDAP server to the LDAP
client without any provocation from the client.
Its format is that of an extended response (

ExtendedResponse

).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

NamingException

getException

()

Retrieves the exception as constructed using information
sent by the server.

String

[]

getReferrals

()

Retrieves the referral(s) sent by the server.

- Methods declared in interface javax.naming.ldap.

ExtendedResponse

getEncodedValue

,

getID

- Methods declared in interface javax.naming.ldap.

HasControls

getControls

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

NamingException

getException

()

Retrieves the exception as constructed using information
sent by the server.

String

[]

getReferrals

()

Retrieves the referral(s) sent by the server.

- Methods declared in interface javax.naming.ldap.

ExtendedResponse

getEncodedValue

,

getID

- Methods declared in interface javax.naming.ldap.

HasControls

getControls

---

#### Method Summary

Retrieves the exception as constructed using information
sent by the server.

Retrieves the referral(s) sent by the server.

Methods declared in interface javax.naming.ldap.

ExtendedResponse

getEncodedValue

,

getID

---

#### Methods declared in interface javax.naming.ldap. ExtendedResponse

Methods declared in interface javax.naming.ldap.

HasControls

getControls

---

#### Methods declared in interface javax.naming.ldap. HasControls

============ METHOD DETAIL ==========

- Method Detail

- getReferrals

```java
String
[] getReferrals()
```

Retrieves the referral(s) sent by the server.

**Returns:** A possibly null array of referrals, each of which is represented
by a URL string. If null, no referral was sent by the server.

- getException

```java
NamingException
getException()
```

Retrieves the exception as constructed using information
sent by the server.

**Returns:** A possibly null exception as constructed using information
sent by the server. If null, a "success" status was indicated by
the server.

Method Detail

- getReferrals

```java
String
[] getReferrals()
```

Retrieves the referral(s) sent by the server.

**Returns:** A possibly null array of referrals, each of which is represented
by a URL string. If null, no referral was sent by the server.

- getException

```java
NamingException
getException()
```

Retrieves the exception as constructed using information
sent by the server.

**Returns:** A possibly null exception as constructed using information
sent by the server. If null, a "success" status was indicated by
the server.

---

#### Method Detail

getReferrals

```java
String
[] getReferrals()
```

Retrieves the referral(s) sent by the server.

**Returns:** A possibly null array of referrals, each of which is represented
by a URL string. If null, no referral was sent by the server.

---

#### getReferrals

String

[] getReferrals()

Retrieves the referral(s) sent by the server.

getException

```java
NamingException
getException()
```

Retrieves the exception as constructed using information
sent by the server.

**Returns:** A possibly null exception as constructed using information
sent by the server. If null, a "success" status was indicated by
the server.

---

#### getException

NamingException

getException()

Retrieves the exception as constructed using information
sent by the server.

---

