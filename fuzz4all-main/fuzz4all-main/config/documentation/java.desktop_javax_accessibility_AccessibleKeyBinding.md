# Interface AccessibleKeyBinding

**Source:** `java.desktop\javax\accessibility\AccessibleKeyBinding.html`

### Class Description

```java
public interface
AccessibleKeyBinding
```

The

AccessibleKeyBinding

interface should be supported by any object
that has a keyboard bindings such as a keyboard mnemonic and/or keyboard
shortcut which can be used to select the object. This interface provides the
standard mechanism for an assistive technology to determine the key bindings
which exist for this object. Any object that has such key bindings should
support this interface.

**Since:** 1.4
**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getAccessibleKeyBindingCount()

Returns the number of key bindings for this object.

**Returns:**
- the zero-based number of key bindings for this object

---

#### Object
getAccessibleKeyBinding​(int i)

Returns a key binding for this object. The value returned is an

java.lang.Object

which must be cast to appropriate type depending
on the underlying implementation of the key.

**Parameters:**
- i

- zero-based index of the key bindings

**Returns:**
- a

javax.lang.Object

which specifies the key binding

**See Also:**
- getAccessibleKeyBindingCount()

---

### Additional Sections

#### Interface AccessibleKeyBinding

```java
public interface
AccessibleKeyBinding
```

The

AccessibleKeyBinding

interface should be supported by any object
that has a keyboard bindings such as a keyboard mnemonic and/or keyboard
shortcut which can be used to select the object. This interface provides the
standard mechanism for an assistive technology to determine the key bindings
which exist for this object. Any object that has such key bindings should
support this interface.

**Since:** 1.4
**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

public interface

AccessibleKeyBinding

The

AccessibleKeyBinding

interface should be supported by any object
that has a keyboard bindings such as a keyboard mnemonic and/or keyboard
shortcut which can be used to select the object. This interface provides the
standard mechanism for an assistive technology to determine the key bindings
which exist for this object. Any object that has such key bindings should
support this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getAccessibleKeyBinding

​(int i)

Returns a key binding for this object.

int

getAccessibleKeyBindingCount

()

Returns the number of key bindings for this object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getAccessibleKeyBinding

​(int i)

Returns a key binding for this object.

int

getAccessibleKeyBindingCount

()

Returns the number of key bindings for this object.

---

#### Method Summary

Returns a key binding for this object.

Returns the number of key bindings for this object.

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleKeyBindingCount

```java
int getAccessibleKeyBindingCount()
```

Returns the number of key bindings for this object.

**Returns:** the zero-based number of key bindings for this object

- getAccessibleKeyBinding

```java
Object
getAccessibleKeyBinding​(int i)
```

Returns a key binding for this object. The value returned is an

java.lang.Object

which must be cast to appropriate type depending
on the underlying implementation of the key.

**Parameters:** i

- zero-based index of the key bindings
**Returns:** a

javax.lang.Object

which specifies the key binding
**See Also:** getAccessibleKeyBindingCount()

Method Detail

- getAccessibleKeyBindingCount

```java
int getAccessibleKeyBindingCount()
```

Returns the number of key bindings for this object.

**Returns:** the zero-based number of key bindings for this object

- getAccessibleKeyBinding

```java
Object
getAccessibleKeyBinding​(int i)
```

Returns a key binding for this object. The value returned is an

java.lang.Object

which must be cast to appropriate type depending
on the underlying implementation of the key.

**Parameters:** i

- zero-based index of the key bindings
**Returns:** a

javax.lang.Object

which specifies the key binding
**See Also:** getAccessibleKeyBindingCount()

---

#### Method Detail

getAccessibleKeyBindingCount

```java
int getAccessibleKeyBindingCount()
```

Returns the number of key bindings for this object.

**Returns:** the zero-based number of key bindings for this object

---

#### getAccessibleKeyBindingCount

int getAccessibleKeyBindingCount()

Returns the number of key bindings for this object.

getAccessibleKeyBinding

```java
Object
getAccessibleKeyBinding​(int i)
```

Returns a key binding for this object. The value returned is an

java.lang.Object

which must be cast to appropriate type depending
on the underlying implementation of the key.

**Parameters:** i

- zero-based index of the key bindings
**Returns:** a

javax.lang.Object

which specifies the key binding
**See Also:** getAccessibleKeyBindingCount()

---

#### getAccessibleKeyBinding

Object

getAccessibleKeyBinding​(int i)

Returns a key binding for this object. The value returned is an

java.lang.Object

which must be cast to appropriate type depending
on the underlying implementation of the key.

---

