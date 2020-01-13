---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

## Java IO Class Overview Table

Having discussed sources, destinations, input, output and the various IO purposes targeted by the Java IO classes, here is a table listing most (if not all) Java IO classes divided by input, output, being byte based or character based, and any more specific purpose they may be addressing, like buffering, parsing etc.

|                  | Byte Based                          | Character Based                   |                                 |                           |
| ---------------- | ----------------------------------- | --------------------------------- | ------------------------------- | ------------------------- |
|                  | Input                               | Output                            | Input                           | Output                    |
| Basic            | InputStream                         | OutputStream                      | Reader InputStreamReader        | Writer OutputStreamWriter |
| Arrays           | ByteArrayInputStream                | ByteArrayOutputStream             | CharArrayReader                 | CharArrayWriter           |
| Files            | FileInputStream RandomAccessFile    | FileOutputStream RandomAccessFile | FileReader                      | FileWriter                |
| Pipes            | PipedInputStream                    | PipedOutputStream                 | PipedReader                     | PipedWriter               |
| Buffering        | BufferedInputStream                 | BufferedOutputStream              | BufferedReader                  | BufferedWriter            |
| Filtering        | FilterInputStream                   | FilterOutputStream                | FilterReader                    | FilterWriter              |
| Parsing          | PushbackInputStream StreamTokenizer |                                   | PushbackReader LineNumberReader |                           |
| Strings          |                                     |                                   | StringReader                    | StringWriter              |
| Data             | DataInputStream                     | DataOutputStream                  |                                 |                           |
| Data - Formatted |                                     | PrintStream                       |                                 | PrintWriter               |
| Objects          | ObjectInputStream                   | ObjectOutputStream                |                                 |                           |
| Utilities        | SequenceInputStream                 |                                   |                                 |                           |