# Interface PreferencesFactory

**Source:** `java.prefs\java\util\prefs\PreferencesFactory.html`

### Class Description

```java
public interface
PreferencesFactory
```

A factory object that generates Preferences objects. Providers of
new

Preferences

implementations should provide corresponding

PreferencesFactory

implementations so that the new

Preferences

implementation can be installed in place of the
platform-specific default implementation.

This class is for

Preferences

implementers only.
Normal users of the

Preferences

facility should have no need to
consult this documentation.

**Since:** 1.4
**See Also:** Preferences

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Preferences
systemRoot()

Returns the system root preference node. (Multiple calls on this
method will return the same object reference.)

**Returns:**
- the system root preference node

---

#### Preferences
userRoot()

Returns the user root preference node corresponding to the calling
user. In a server, the returned value will typically depend on
some implicit client-context.

**Returns:**
- the user root preference node corresponding to the calling
user

---

### Additional Sections

#### Interface PreferencesFactory

```java
public interface
PreferencesFactory
```

A factory object that generates Preferences objects. Providers of
new

Preferences

implementations should provide corresponding

PreferencesFactory

implementations so that the new

Preferences

implementation can be installed in place of the
platform-specific default implementation.

This class is for

Preferences

implementers only.
Normal users of the

Preferences

facility should have no need to
consult this documentation.

**Since:** 1.4
**See Also:** Preferences

public interface

PreferencesFactory

A factory object that generates Preferences objects. Providers of
new

Preferences

implementations should provide corresponding

PreferencesFactory

implementations so that the new

Preferences

implementation can be installed in place of the
platform-specific default implementation.

This class is for

Preferences

implementers only.
Normal users of the

Preferences

facility should have no need to
consult this documentation.

This class is for

Preferences

implementers only.
Normal users of the

Preferences

facility should have no need to
consult this documentation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Preferences

systemRoot

()

Returns the system root preference node.

Preferences

userRoot

()

Returns the user root preference node corresponding to the calling
user.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Preferences

systemRoot

()

Returns the system root preference node.

Preferences

userRoot

()

Returns the user root preference node corresponding to the calling
user.

---

#### Method Summary

Returns the system root preference node.

Returns the user root preference node corresponding to the calling
user.

============ METHOD DETAIL ==========

- Method Detail

- systemRoot

```java
Preferences
systemRoot()
```

Returns the system root preference node. (Multiple calls on this
method will return the same object reference.)

**Returns:** the system root preference node

- userRoot

```java
Preferences
userRoot()
```

Returns the user root preference node corresponding to the calling
user. In a server, the returned value will typically depend on
some implicit client-context.

**Returns:** the user root preference node corresponding to the calling
user

Method Detail

- systemRoot

```java
Preferences
systemRoot()
```

Returns the system root preference node. (Multiple calls on this
method will return the same object reference.)

**Returns:** the system root preference node

- userRoot

```java
Preferences
userRoot()
```

Returns the user root preference node corresponding to the calling
user. In a server, the returned value will typically depend on
some implicit client-context.

**Returns:** the user root preference node corresponding to the calling
user

---

#### Method Detail

systemRoot

```java
Preferences
systemRoot()
```

Returns the system root preference node. (Multiple calls on this
method will return the same object reference.)

**Returns:** the system root preference node

---

#### systemRoot

Preferences

systemRoot()

Returns the system root preference node. (Multiple calls on this
method will return the same object reference.)

userRoot

```java
Preferences
userRoot()
```

Returns the user root preference node corresponding to the calling
user. In a server, the returned value will typically depend on
some implicit client-context.

**Returns:** the user root preference node corresponding to the calling
user

---

#### userRoot

Preferences

userRoot()

Returns the user root preference node corresponding to the calling
user. In a server, the returned value will typically depend on
some implicit client-context.

---

