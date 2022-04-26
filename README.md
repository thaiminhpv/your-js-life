<p align="center"><img width="35%" src="src/static/images/favicon.png" alt="icon"></p>
<h2 align="center">Your JS Life</h2>
<p align="center">A portfolio is All You Need</p>

## Deployment

| Branch                        | Latest commit is deployed to `url`                                                                                           |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `master`                      | [japanese-software.engineer](https://japanese-software.engineer)                                                             |
| `develop`                     | [develop.japanese-software.engineer](https://develop.japanese-software.engineer)                                             |
| `feature/generated-portfolio` | [generated-portfolio.japanese-software.engineer/portfolio](https://generated-portfolio.japanese-software.engineer/portfolio) |
| `feature/input-page`          | [input-page.japanese-software.engineer/create-portfolio](https://input-page.japanese-software.engineer/create-portfolio)     |
| `feature/landing-page`        | [landing-page.japanese-software.engineer/](https://landing-page.japanese-software.engineer)                                  |
| `feature/connect_database`    | [connect-database.japanese-software.engineer](https://connect-database.japanese-software.engineer)                           |

## How to run

1. Setup MySQL database (can be _local_ or _remote_)
2. Run [database-dump.sql](./sql-dump/database-dump.sql)
3. Setup Cloudinary
4. Copy `.env.example` to `.env` and fill in the secrets
5. Run server

    ```bash
    # Create virtual environment
    python -m venv env

    # Activate virtual environment
    env\Scripts\activate.bat          # for Windows
        # or
    source env/bin/activate           # for Linux

    # Install dependencies
    pip install -r requirements.txt

    # Run
    python app.py
    ```

## Contributors

### Mentor

- Hưng thiên thần _(mentor)_

### Takecare

- Dương Thuỳ Trang
- Hồ Khánh Vũ 

### Members

- Thái Minh _(leader)_
- Tuấn Ninh
- Đặng Trang
- Minh Đức
- Xuân Hậu
- Duy Khánh

## Meeting Reports

- [Reports folder](https://drive.google.com/drive/folders/1lH4HKKwLGwdbXkEeUezOFPBTNW-S9KI1)
