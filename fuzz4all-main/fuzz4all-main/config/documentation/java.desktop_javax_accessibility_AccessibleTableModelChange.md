# Interface AccessibleTableModelChange

**Source:** `java.desktop\javax\accessibility\AccessibleTableModelChange.html`

### Class Description

```java
public interface
AccessibleTableModelChange
```

The

AccessibleTableModelChange

interface describes a change to the
table model. The attributes of the model change can be obtained by the
following methods:

- public int getType();

public int getFirstRow();

public int getLastRow();

public int getFirstColumn();

public int getLastColumn();

The model change type returned by getType() will be one of:

- INSERT

- one or more rows and/or columns have been inserted

UPDATE

- some of the table data has changed

DELETE

- one or more rows and/or columns have been deleted

The affected area of the table can be determined by the other four methods
which specify ranges of rows and columns

**All Known Implementing Classes:** JTable.AccessibleJTable.AccessibleJTableModelChange

---

### Field Details

#### static final int INSERT

Identifies the insertion of new rows and/or columns.

**See Also:**
- Constant Field Values

---

#### static final int UPDATE

Identifies a change to existing data.

**See Also:**
- Constant Field Values

---

#### static final int DELETE

Identifies the deletion of rows and/or columns.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getType()

Returns the type of event.

**Returns:**
- the type of event

**See Also:**
- INSERT

,

UPDATE

,

DELETE

---

#### int getFirstRow()

Returns the first row that changed.

**Returns:**
- the first row that changed

---

#### int getLastRow()

Returns the last row that changed.

**Returns:**
- the last row that changed

---

#### int getFirstColumn()

Returns the first column that changed.

**Returns:**
- the first column that changed

---

#### int getLastColumn()

Returns the last column that changed.

**Returns:**
- the last column that changed

---

### Additional Sections

#### Interface AccessibleTableModelChange

**All Known Implementing Classes:** JTable.AccessibleJTable.AccessibleJTableModelChange

```java
public interface
AccessibleTableModelChange
```

The

AccessibleTableModelChange

interface describes a change to the
table model. The attributes of the model change can be obtained by the
following methods:

- public int getType();

public int getFirstRow();

public int getLastRow();

public int getFirstColumn();

public int getLastColumn();

The model change type returned by getType() will be one of:

- INSERT

- one or more rows and/or columns have been inserted

UPDATE

- some of the table data has changed

DELETE

- one or more rows and/or columns have been deleted

The affected area of the table can be determined by the other four methods
which specify ranges of rows and columns

**Since:** 1.3
**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleTable()

public interface

AccessibleTableModelChange

The

AccessibleTableModelChange

interface describes a change to the
table model. The attributes of the model change can be obtained by the
following methods:

- public int getType();

public int getFirstRow();

public int getLastRow();

public int getFirstColumn();

public int getLastColumn();

The model change type returned by getType() will be one of:

- INSERT

- one or more rows and/or columns have been inserted

UPDATE

- some of the table data has changed

DELETE

- one or more rows and/or columns have been deleted

The affected area of the table can be determined by the other four methods
which specify ranges of rows and columns

public int getType();

public int getFirstRow();

public int getLastRow();

public int getFirstColumn();

public int getLastColumn();

INSERT

- one or more rows and/or columns have been inserted

UPDATE

- some of the table data has changed

DELETE

- one or more rows and/or columns have been deleted

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DELETE

Identifies the deletion of rows and/or columns.

static int

INSERT

Identifies the insertion of new rows and/or columns.

static int

UPDATE

Identifies a change to existing data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getFirstColumn

()

Returns the first column that changed.

int

getFirstRow

()

Returns the first row that changed.

int

getLastColumn

()

Returns the last column that changed.

int

getLastRow

()

Returns the last row that changed.

int

getType

()

Returns the type of event.

Field Summary

Fields

Modifier and Type

Field

Description

static int

DELETE

Identifies the deletion of rows and/or columns.

static int

INSERT

Identifies the insertion of new rows and/or columns.

static int

UPDATE

Identifies a change to existing data.

---

#### Field Summary

Identifies the deletion of rows and/or columns.

Identifies the insertion of new rows and/or columns.

Identifies a change to existing data.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getFirstColumn

()

Returns the first column that changed.

int

getFirstRow

()

Returns the first row that changed.

int

getLastColumn

()

Returns the last column that changed.

int

getLastRow

()

Returns the last row that changed.

int

getType

()

Returns the type of event.

---

#### Method Summary

Returns the first column that changed.

Returns the first row that changed.

Returns the last column that changed.

Returns the last row that changed.

Returns the type of event.

============ FIELD DETAIL ===========

- Field Detail

- INSERT

```java
static final int INSERT
```

Identifies the insertion of new rows and/or columns.

**See Also:** Constant Field Values

- UPDATE

```java
static final int UPDATE
```

Identifies a change to existing data.

**See Also:** Constant Field Values

- DELETE

```java
static final int DELETE
```

Identifies the deletion of rows and/or columns.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
int getType()
```

Returns the type of event.

**Returns:** the type of event
**See Also:** INSERT

,

UPDATE

,

DELETE

- getFirstRow

```java
int getFirstRow()
```

Returns the first row that changed.

**Returns:** the first row that changed

- getLastRow

```java
int getLastRow()
```

Returns the last row that changed.

**Returns:** the last row that changed

- getFirstColumn

```java
int getFirstColumn()
```

Returns the first column that changed.

**Returns:** the first column that changed

- getLastColumn

```java
int getLastColumn()
```

Returns the last column that changed.

**Returns:** the last column that changed

Field Detail

- INSERT

```java
static final int INSERT
```

Identifies the insertion of new rows and/or columns.

**See Also:** Constant Field Values

- UPDATE

```java
static final int UPDATE
```

Identifies a change to existing data.

**See Also:** Constant Field Values

- DELETE

```java
static final int DELETE
```

Identifies the deletion of rows and/or columns.

**See Also:** Constant Field Values

---

#### Field Detail

INSERT

```java
static final int INSERT
```

Identifies the insertion of new rows and/or columns.

**See Also:** Constant Field Values

---

#### INSERT

static final int INSERT

Identifies the insertion of new rows and/or columns.

UPDATE

```java
static final int UPDATE
```

Identifies a change to existing data.

**See Also:** Constant Field Values

---

#### UPDATE

static final int UPDATE

Identifies a change to existing data.

DELETE

```java
static final int DELETE
```

Identifies the deletion of rows and/or columns.

**See Also:** Constant Field Values

---

#### DELETE

static final int DELETE

Identifies the deletion of rows and/or columns.

Method Detail

- getType

```java
int getType()
```

Returns the type of event.

**Returns:** the type of event
**See Also:** INSERT

,

UPDATE

,

DELETE

- getFirstRow

```java
int getFirstRow()
```

Returns the first row that changed.

**Returns:** the first row that changed

- getLastRow

```java
int getLastRow()
```

Returns the last row that changed.

**Returns:** the last row that changed

- getFirstColumn

```java
int getFirstColumn()
```

Returns the first column that changed.

**Returns:** the first column that changed

- getLastColumn

```java
int getLastColumn()
```

Returns the last column that changed.

**Returns:** the last column that changed

---

#### Method Detail

getType

```java
int getType()
```

Returns the type of event.

**Returns:** the type of event
**See Also:** INSERT

,

UPDATE

,

DELETE

---

#### getType

int getType()

Returns the type of event.

getFirstRow

```java
int getFirstRow()
```

Returns the first row that changed.

**Returns:** the first row that changed

---

#### getFirstRow

int getFirstRow()

Returns the first row that changed.

getLastRow

```java
int getLastRow()
```

Returns the last row that changed.

**Returns:** the last row that changed

---

#### getLastRow

int getLastRow()

Returns the last row that changed.

getFirstColumn

```java
int getFirstColumn()
```

Returns the first column that changed.

**Returns:** the first column that changed

---

#### getFirstColumn

int getFirstColumn()

Returns the first column that changed.

getLastColumn

```java
int getLastColumn()
```

Returns the last column that changed.

**Returns:** the last column that changed

---

#### getLastColumn

int getLastColumn()

Returns the last column that changed.

---

