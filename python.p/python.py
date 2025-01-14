public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float jumpForce = 10f;
    private Rigidbody2D rb;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Harakat qilish
        float move = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(move * moveSpeed, rb.velocity.y);
        // Sakrash
        if (Input.GetButtonDown("Jump"))
        {
            rb.velocity = Vector2.up * jumpForce;
        }
    }
}
