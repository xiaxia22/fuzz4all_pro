# Interface UIDefaults.ActiveValue

**Source:** `java.desktop\javax\swing\UIDefaults.ActiveValue.html`

### Class Description

```java
public static interface
UIDefaults.ActiveValue
```

This class enables one to store an entry in the defaults
table that's constructed each time it's looked up with one of
the

getXXX(key)

methods. Here's an example of
an

ActiveValue

that constructs a

DefaultListCellRenderer

:

```java
Object cellRendererActiveValue = new UIDefaults.ActiveValue() {
public Object createValue(UIDefaults table) {
return new DefaultListCellRenderer();
}
};

uiDefaultsTable.put("MyRenderer", cellRendererActiveValue);
```

**Enclosing class:** UIDefaults

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
createValue​(
UIDefaults
table)

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Parameters:**
- table

- a

UIDefaults

table

**Returns:**
- the created

Object

---

### Additional Sections

#### Interface UIDefaults.ActiveValue

**Enclosing class:** UIDefaults

```java
public static interface
UIDefaults.ActiveValue
```

This class enables one to store an entry in the defaults
table that's constructed each time it's looked up with one of
the

getXXX(key)

methods. Here's an example of
an

ActiveValue

that constructs a

DefaultListCellRenderer

:

```java
Object cellRendererActiveValue = new UIDefaults.ActiveValue() {
public Object createValue(UIDefaults table) {
return new DefaultListCellRenderer();
}
};

uiDefaultsTable.put("MyRenderer", cellRendererActiveValue);
```

**See Also:** UIDefaults.get(java.lang.Object)

public static interface

UIDefaults.ActiveValue

This class enables one to store an entry in the defaults
table that's constructed each time it's looked up with one of
the

getXXX(key)

methods. Here's an example of
an

ActiveValue

that constructs a

DefaultListCellRenderer

:

```java
Object cellRendererActiveValue = new UIDefaults.ActiveValue() {
public Object createValue(UIDefaults table) {
return new DefaultListCellRenderer();
}
};

uiDefaultsTable.put("MyRenderer", cellRendererActiveValue);
```

Object cellRendererActiveValue = new UIDefaults.ActiveValue() {
public Object createValue(UIDefaults table) {
return new DefaultListCellRenderer();
}
};

uiDefaultsTable.put("MyRenderer", cellRendererActiveValue);

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

createValue

​(

UIDefaults

table)

Creates the value retrieved from the

UIDefaults

table.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

createValue

​(

UIDefaults

table)

Creates the value retrieved from the

UIDefaults

table.

---

#### Method Summary

Creates the value retrieved from the

UIDefaults

table.

============ METHOD DETAIL ==========

- Method Detail

- createValue

```java
Object
createValue​(
UIDefaults
table)
```

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Parameters:** table

- a

UIDefaults

table
**Returns:** the created

Object

Method Detail

- createValue

```java
Object
createValue​(
UIDefaults
table)
```

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Parameters:** table

- a

UIDefaults

table
**Returns:** the created

Object

---

#### Method Detail

createValue

```java
Object
createValue​(
UIDefaults
table)
```

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

**Parameters:** table

- a

UIDefaults

table
**Returns:** the created

Object

---

#### createValue

Object

createValue​(

UIDefaults

table)

Creates the value retrieved from the

UIDefaults

table.
The object is created each time it is accessed.

---

