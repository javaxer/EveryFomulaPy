#문자 처리와 관련된 함수들.
#코드는 effective python이라는 책에서 가져왔다.

def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value=bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value #Str 인스턴스

def to_bytes(bytes_or_str):
    if ininstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value #bytes 인스턴수
