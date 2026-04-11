# Interface HasControls

**Source:** `java.naming\javax\naming\ldap\HasControls.html`

### Class Description

```java
public interface
HasControls
```

This interface is for returning controls with objects returned
in NamingEnumerations.
For example, suppose a server sends back controls with the results
of a search operation, the service provider would return a NamingEnumeration of
objects that are both SearchResult and implement HasControls.

```java
NamingEnumeration elts = ectx.search((Name)name, filter, sctls);
while (elts.hasMore()) {
Object entry = elts.next();

// Get search result
SearchResult res = (SearchResult)entry;
// do something with it

// Get entry controls
if (entry instanceof HasControls) {
Control[] entryCtls = ((HasControls)entry).getControls();
// do something with controls
}
}
```

**All Known Subinterfaces:** UnsolicitedNotification

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Control
[] getControls()
throws
NamingException

Retrieves an array of

Control

s from the object that
implements this interface. It is null if there are no controls.

**Returns:**
- A possibly null array of

Control

objects.

**Throws:**
- NamingException

- If cannot return controls due to an error.

---

### Additional Sections

#### Interface HasControls

**All Known Subinterfaces:** UnsolicitedNotification

```java
public interface
HasControls
```

This interface is for returning controls with objects returned
in NamingEnumerations.
For example, suppose a server sends back controls with the results
of a search operation, the service provider would return a NamingEnumeration of
objects that are both SearchResult and implement HasControls.

```java
NamingEnumeration elts = ectx.search((Name)name, filter, sctls);
while (elts.hasMore()) {
Object entry = elts.next();

// Get search result
SearchResult res = (SearchResult)entry;
// do something with it

// Get entry controls
if (entry instanceof HasControls) {
Control[] entryCtls = ((HasControls)entry).getControls();
// do something with controls
}
}
```

**Since:** 1.3

public interface

HasControls

This interface is for returning controls with objects returned
in NamingEnumerations.
For example, suppose a server sends back controls with the results
of a search operation, the service provider would return a NamingEnumeration of
objects that are both SearchResult and implement HasControls.

```java
NamingEnumeration elts = ectx.search((Name)name, filter, sctls);
while (elts.hasMore()) {
Object entry = elts.next();

// Get search result
SearchResult res = (SearchResult)entry;
// do something with it

// Get entry controls
if (entry instanceof HasControls) {
Control[] entryCtls = ((HasControls)entry).getControls();
// do something with controls
}
}
```

NamingEnumeration elts = ectx.search((Name)name, filter, sctls);
while (elts.hasMore()) {
Object entry = elts.next();

// Get search result
SearchResult res = (SearchResult)entry;
// do something with it

// Get entry controls
if (entry instanceof HasControls) {
Control[] entryCtls = ((HasControls)entry).getControls();
// do something with controls
}
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Control

[]

getControls

()

Retrieves an array of

Control

s from the object that
implements this interface.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Control

[]

getControls

()

Retrieves an array of

Control

s from the object that
implements this interface.

---

#### Method Summary

Retrieves an array of

Control

s from the object that
implements this interface.

============ METHOD DETAIL ==========

- Method Detail

- getControls

```java
Control
[] getControls()
throws
NamingException
```

Retrieves an array of

Control

s from the object that
implements this interface. It is null if there are no controls.

**Returns:** A possibly null array of

Control

objects.
**Throws:** NamingException

- If cannot return controls due to an error.

Method Detail

- getControls

```java
Control
[] getControls()
throws
NamingException
```

Retrieves an array of

Control

s from the object that
implements this interface. It is null if there are no controls.

**Returns:** A possibly null array of

Control

objects.
**Throws:** NamingException

- If cannot return controls due to an error.

---

#### Method Detail

getControls

```java
Control
[] getControls()
throws
NamingException
```

Retrieves an array of

Control

s from the object that
implements this interface. It is null if there are no controls.

**Returns:** A possibly null array of

Control

objects.
**Throws:** NamingException

- If cannot return controls due to an error.

---

#### getControls

Control

[] getControls()
throws

NamingException

Retrieves an array of

Control

s from the object that
implements this interface. It is null if there are no controls.

---

