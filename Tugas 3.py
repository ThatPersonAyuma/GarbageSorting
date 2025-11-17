from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class Book:
    kode: int
    judul: str
    pengarang: str
    tahun: int

    def __str__(self):
        return f"[{self.kode}] {self.judul} - {self.pengarang} ({self.tahun})"

class _Node:
    def __init__(self, book: Book):
        self.book = book
        self.left: Optional[_Node] = None
        self.right: Optional[_Node] = None

class LibraryBST:
    def __init__(self):
        self.root: Optional[_Node] = None
        self._count = 0

    def add_book(self, kode:int, judul:str, pengarang:str, tahun:int):
        book = Book(kode, judul, pengarang, tahun)
        if not self.root:
            self.root = _Node(book)
            self._count = 1
            return
        cur = self.root
        while True:
            if kode < cur.book.kode:
                if cur.left is None:
                    cur.left = _Node(book)
                    self._count += 1
                    return
                cur = cur.left
            elif kode > cur.book.kode:
                if cur.right is None:
                    cur.right = _Node(book)
                    self._count += 1
                    return
                cur = cur.right
            else:
                # Jika kode sama,dapat dioverwrite atau abaikan. Pilih overwrite:
                cur.book = book
                return

    def _search_node_with_parent(self, kode:int) -> Tuple[Optional[_Node], Optional[_Node]]:
        parent = None
        cur = self.root
        while cur:
            if kode == cur.book.kode:
                return cur, parent
            parent = cur
            if kode < cur.book.kode:
                cur = cur.left
            else:
                cur = cur.right
        return None, parent

    def search_book(self, kode:int) -> Tuple[Optional[Book], Optional[Book], Optional[Book]]:
        cur = self.root
        pred = None
        succ = None
        while cur:
            if kode == cur.book.kode:
                # find predecessor (max in left subtree) and successor (min in right subtree)
                if cur.left:
                    tmp = cur.left
                    while tmp.right:
                        tmp = tmp.right
                    pred = tmp.book
                if cur.right:
                    tmp = cur.right
                    while tmp.left:
                        tmp = tmp.left
                    succ = tmp.book
                return cur.book, pred, succ
            elif kode < cur.book.kode:
                succ = cur.book  # current could be successor
                cur = cur.left
            else:
                pred = cur.book   # current could be predecessor
                cur = cur.right
        # Tidak ditemukan
        return None, pred, succ

    def find_min_code(self) -> Optional[Book]:
        cur = self.root
        if not cur:
            return None
        while cur.left:
            cur = cur.left
        return cur.book

    def find_max_code(self) -> Optional[Book]:
        cur = self.root
        if not cur:
            return None
        while cur.right:
            cur = cur.right
        return cur.book

    def _inorder(self, node: Optional[_Node], out: List[Book]):
        if not node:
            return
        self._inorder(node.left, out)
        out.append(node.book)
        self._inorder(node.right, out)

    def display_sorted(self) -> List[Book]:
        out: List[Book] = []
        self._inorder(self.root, out)
        return out

    def count_books(self) -> int:
        return self._count

    def get_books_in_range(self, kode_min:int, kode_max:int) -> List[Book]:
        res: List[Book] = []
        def dfs(node: Optional[_Node]):
            if not node:
                return
            if node.book.kode > kode_min:
                dfs(node.left)
            if kode_min <= node.book.kode <= kode_max:
                res.append(node.book)
            if node.book.kode < kode_max:
                dfs(node.right)
        dfs(self.root)
        return res

# Program Utama (mengisi data dari soal)

if __name__ == "__main__":
    lib = LibraryBST()
    data = [
        (501, "Algoritma Dasar", "Wijaya", 2020),
        (305, "Struktur Data", "Santoso", 2019),
        (720, "Database System", "Rahman", 2021),
        (150, "Pemrograman Python", "Sari", 2022),
        (450, "Web Development", "Kusuma", 2020),
        (680, "Machine Learning", "Pratama", 2023),
        (890, "Cloud Computing", "Dewi", 2021),
        (120, "Jaringan Komputer", "Hidayat", 2019),
        (550, "Cyber Security", "Permana", 2022),
    ]
    for kode, judul, pengarang, tahun in data:
        lib.add_book(kode, judul, pengarang, tahun)

    # 1. Cari buku kode 550
    found, pred, succ = lib.search_book(550)
    if found:
        print("Ditemukan:", found)
    else:
        print("Kode 550 tidak ditemukan. Rekomendasi terdekat:", pred, succ)

    # 2. Cari buku kode 300 (tidak ada)
    found2, pred2, succ2 = lib.search_book(300)
    if found2:
        print("Ditemukan:", found2)
    else:
        print("Kode 300 tidak ditemukan.")
        if pred2:
            print("Predecessor (lebih kecil terdekat):", pred2)
        if succ2:
            print("Successor (lebih besar terdekat):", succ2)

    # 3. Tampilkan semua buku terurut
    print("\nSemua buku terurut (kode):")
    for b in lib.display_sorted():
        print(b)

    # 4. Buku dengan kode terkecil dan terbesar
    print("\nKode terkecil:", lib.find_min_code())
    print("Kode terbesar:", lib.find_max_code())

    # 5. Buku dalam rentang 200-600
    print("\nBuku dalam rentang 200 - 600:")
    for b in lib.get_books_in_range(200, 600):
        print(b)

    # Count total
    print("\nTotal buku:", lib.count_books())
